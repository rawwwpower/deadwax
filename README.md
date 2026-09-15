# Dead Wax

Proyecto personal de Ana para evaluar ediciones de vinilo antes de comprarlas
(autenticación de prensados, jerarquía de plantas, red flags de sellos
truchos) y llevar el catálogo de su colección — y la de Seba.

## Estado actual

Hoy el proyecto es un **skill de Claude Code**: metodología encapsulada en
`SKILL.md`/`references/` más un CLI (`scripts/coleccion.py`) sobre una base
SQLite local (`data/coleccion.db`) con la colección real. Vive en
[`.claude/skills/dead-wax/`](.claude/skills/dead-wax/) — ver el
[README del skill](.claude/skills/dead-wax/README.md) para el detalle de uso.

Esta es la primera pieza de algo más grande — ver [ROADMAP.md](ROADMAP.md)
para hacia dónde va. La raíz del repo queda libre para que futuras partes
(indexación de Discogs, front de la colección, etc.) no tengan que
mezclarse con el skill.

## Estructura del repo

```
deadwax/
├── README.md                    ← este archivo
├── ROADMAP.md                   ← fases futuras del proyecto
└── .claude/
    └── skills/
        └── dead-wax/            ← el skill (metodología + CLI + datos)
            ├── SKILL.md
            ├── README.md
            ├── references/
            ├── scripts/
            └── data/coleccion.db
```

## Uso rápido

Con Claude Code abierto en este repo, el skill se activa solo al mencionar
un disco, un anuncio de venta, o una pregunta sobre la colección. Para
tocar la base a mano:

```bash
cd .claude/skills/dead-wax
python3 scripts/coleccion.py list
python3 scripts/coleccion.py stats
```
