# Dead Wax

Una guía para comprar vinilos como se compra una obra de arte: sabiendo qué
edición es, quién la hizo y cuánto vale.

Por ahora son dos herramientas: una guía de evaluación que usa Claude y una
app para ver la colección y la wantlist. Todavía no están conectadas entre sí;
el plan para unirlas está en [ROADMAP.md](ROADMAP.md).

## 1. El skill de Claude Code (metodología + colección)

En [`.claude/skills/dead-wax/`](.claude/skills/dead-wax/): la metodología de
evaluación (`SKILL.md`/`references/`) más un CLI (`scripts/coleccion.py`)
sobre una base SQLite (`data/coleccion.db`) con la colección real. Claude
Code lo detecta solo al abrir este repo — no hace falta invocarlo a mano.
Ver el [README del skill](.claude/skills/dead-wax/README.md) para el uso.

```bash
cd .claude/skills/dead-wax
python3 scripts/coleccion.py list
python3 scripts/coleccion.py stats
```

## 2. La app web (colección + wantlist)

En la raíz (`index.html`, `css/`, `js/`): una app simple para llevar la
colección de discos y la wantlist desde el navegador, con un filtro
**Yo / Seba / Fusión** para armar sesiones de escucha juntos. Todo se guarda
en `localStorage` (sin backend), con export/import a JSON para pasarse
colecciones entre los dos.

```bash
# abrí index.html en el navegador, o serví la carpeta con cualquier
# servidor estático
```

La lógica de guardado vive en el objeto `Store` de `js/app.js` (`getAll`,
`saveAll`, `upsert`, `remove`) — para pasar a un backend real alcanza con
reemplazar esos métodos, sin tocar el resto de la UI.

## Estructura del repo

```
deadwax/
├── README.md
├── ROADMAP.md
├── index.html            ← app web (colección + wantlist)
├── nana/                 ← nana: la webapp con forma de iPod nano (ver nana/README.md)
├── css/
├── js/
└── .claude/
    └── skills/
        └── dead-wax/      ← skill de Claude Code (metodología + CLI + datos)
            ├── SKILL.md
            ├── README.md
            ├── references/
            ├── scripts/
            └── data/coleccion.db
```
