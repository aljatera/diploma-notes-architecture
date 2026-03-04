PROJECT CONTEXT

Diplomska naloga (VSŠ Informatika – DOBA).

Tema:
Primerjava arhitekturnih pristopov pri razvoju manjše aplikacije.

Aplikacija:
CLI aplikacija za upravljanje zapiskov.

Tehnologije:
Python
SQLite

Funkcionalnosti aplikacije:

add
list
view
tag
filter (po tagu)
search (po naslovu)

Arhitektura monolita:

app.py
CLI logika in ukazni dispečer

database.py
dostop do SQLite baze

Podatkovni model:

notes
tags
note_tags

Cilj diplome:

primerjava

1. monolitne implementacije
2. modularnega monolita

Metodologija:

primerjava po merilih

- preglednost kode
- ločitev odgovornosti
- coupling
- razširljivost
- vzdrževanje

Trenutno stanje projekta:

monolit MVP implementiran
narejena prva arhitekturna analiza

Naslednji koraki:

1 implementacija modularnega monolita
2 primerjalna analiza
3 priprava prilog s kodo
