# Diploma – arhitektura aplikacije za zapiske

Projekt za diplomsko nalogo (VSŠ Informatika – DOBA).

Tema:
Primerjava arhitekturnih pristopov pri razvoju manjše CLI aplikacije v Pythonu.

Tehnologije:
Python
SQLite
CLI aplikacija

Struktura projekta:

code/
  monolith/
  modular/

thesis/
  dokumenti diplome

docs/
  raziskovalne in arhitekturne opombe

Zagon aplikacije:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py add "Title" "Content"
