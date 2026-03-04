from __future__ import annotations

import sqlite3
from pathlib import Path

DB_FILE = Path("notes.db")

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS note_tags (
    note_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (note_id, tag_id),
    FOREIGN KEY (note_id) REFERENCES notes(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);
"""


def get_connection(db_path: Path = DB_FILE) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(db_path: Path = DB_FILE) -> None:
    with get_connection(db_path) as conn:
        conn.executescript(SCHEMA_SQL)
        conn.commit()


from datetime import datetime


def add_note(title: str, content: str, db_path=DB_FILE) -> None:
    now = datetime.utcnow().isoformat()

    with get_connection(db_path) as conn:
        conn.execute(
            "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, now),
        )
        conn.commit()

def list_notes(db_path=DB_FILE):
    with get_connection(db_path) as conn:
        cur = conn.execute(
            "SELECT id, title, created_at FROM notes ORDER BY id DESC"
        )
        return cur.fetchall()

def get_note(note_id: int, db_path=DB_FILE):
    with get_connection(db_path) as conn:
        cur = conn.execute(
            "SELECT id, title, content, created_at FROM notes WHERE id = ?",
            (note_id,),
        )
        return cur.fetchone()

def add_tag_to_note(note_id: int, tag_name: str, db_path=DB_FILE):
    with get_connection(db_path) as conn:
        # 1. Ustvari tag, če še ne obstaja
        conn.execute(
            "INSERT OR IGNORE INTO tags (name) VALUES (?)",
            (tag_name,),
        )

        # 2. Pridobi ID taga
        cur = conn.execute(
            "SELECT id FROM tags WHERE name = ?",
            (tag_name,),
        )
        tag = cur.fetchone()

        if tag is None:
            return

        tag_id = tag["id"]

        # 3. Poveži zapisek in tag
        conn.execute(
            "INSERT OR IGNORE INTO note_tags (note_id, tag_id) VALUES (?, ?)",
            (note_id, tag_id),
        )

        conn.commit()

def list_notes_by_tag(tag_name: str, db_path=DB_FILE):
    with get_connection(db_path) as conn:
        cur = conn.execute(
            """
            SELECT n.id, n.title, n.created_at
            FROM notes n
            JOIN note_tags nt ON nt.note_id = n.id
            JOIN tags t ON t.id = nt.tag_id
            WHERE t.name = ?
            ORDER BY n.id DESC
            """,
            (tag_name,),
        )
        return cur.fetchall()

def search_notes(query: str, db_path=DB_FILE):
    pattern = f"%{query}%"
    with get_connection(db_path) as conn:
        cur = conn.execute(
            "SELECT id, title, created_at FROM notes WHERE title LIKE ? ORDER BY id DESC",
            (pattern,),
        )
        return cur.fetchall()