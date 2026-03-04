import sys
from database import init_db, add_note, list_notes, get_note, add_tag_to_note, list_notes_by_tag, search_notes


def print_usage():
    print()
    print("CLI Notes Application")
    print("---------------------")
    print()
    print("Available commands:")
    print('  add "Title" "Content"')
    print("  list")
    print("  view <id>")
    print("  tag <id> <tag>")
    print("  filter <tag>")
    print('  search "keyword"')
    print("  help")
    print()

def main():
    init_db()

    # sys.argv[0] = app.py
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "help":
        print_usage()
        return

    if command == "add":
        if len(sys.argv) < 4:
            print_usage()
            return
        title = sys.argv[2]
        content = sys.argv[3]
        add_note(title, content)
        print("Note added.")
        return

    if command == "list":
        rows = list_notes()
        if not rows:
            print("No notes yet.")
        else:
            for r in rows:
                print(f'{r["id"]}: {r["title"]} ({r["created_at"]})')
        return

    if command == "view":
        if len(sys.argv) < 3:
            print_usage()
            return
        try:
            note_id = int(sys.argv[2])
        except ValueError:
            print("ID must be an integer.")
            return

        note = get_note(note_id)
        if note is None:
            print("Note not found.")
            return

        print(f'ID: {note["id"]}')
        print(f'Title: {note["title"]}')
        print(f'Created: {note["created_at"]}')
        print("-" * 40)
        print(note["content"])
        return
    
    if command == "tag":
        if len(sys.argv) < 4:
            print_usage()
            return
        try:
            note_id = int(sys.argv[2])
        except ValueError:
            print("ID must be an integer.")
            return

        tag_name = sys.argv[3]
        add_tag_to_note(note_id, tag_name)
        print("Tag added.")
        return
        
    if command == "filter":
        if len(sys.argv) < 3:
            print_usage()
            return

        tag_name = sys.argv[2]
        rows = list_notes_by_tag(tag_name)

        if not rows:
            print("No notes for this tag.")
        else:
            for r in rows:
                print(f'{r["id"]}: {r["title"]} ({r["created_at"]})')
        return    

    if command == "search":
        if len(sys.argv) < 3:
            print_usage()
            return

        query = sys.argv[2]
        rows = search_notes(query)

        if not rows:
            print("No matches.")
        else:
            for r in rows:
                print(f'{r["id"]}: {r["title"]} ({r["created_at"]})')
        return
    
    print_usage()


    
    

if __name__ == "__main__":
    main()
