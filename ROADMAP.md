# Roadmap

Cómo se imagina que crezca el proyecto, para que no quede pegado a ser "un
skill". Nada de esto es una promesa con fecha, es el orden de prioridad tal
como está pensado hoy.

## Fase 1 — Skill de Claude Code (actual)

- Metodología de evaluación (3 criterios, jerarquía de plantas, red flags,
  casos específicos) en `.claude/skills/dead-wax/`.
- CLI (`scripts/coleccion.py`) + SQLite (`data/coleccion.db`) como fuente de
  verdad de la colección de Ana y de Seba.
- Funciona 100% dependiente de Discogs online para identificar prensados.

## Fase 2 — Independencia de Discogs online

- Indexar el [Discogs Data Dump](https://www.discogs.com/data/) localmente
  para poder buscar/identificar releases sin depender de la web en cada
  consulta (y sin rate limits).
- Evaluar si conviene un dataset propio derivado (solo lo necesario: master
  → releases → país/sello/catálogo/matrix) en vez del dump completo.

## Fase 3 — Portabilidad de los datos

- Export/import de `coleccion.db` a JSON o CSV, para poder ver la colección
  fuera de SQL (ej. una plancha en Google Sheets) o migrarla si hace falta.
- Backups simples de `data/coleccion.db`.

## Fase 4 — Visualización / front simple

Ya arrancó: hay una app web en la raíz (`index.html`, `css/`, `js/`) con
colección + wantlist + fusión Yo/Seba, guardando en `localStorage` con
export/import a JSON.

Pendiente para que deje de ser una pieza separada del skill:
- Hoy la app y `data/coleccion.db` son dos fuentes de verdad distintas
  (localStorage del navegador vs. SQLite que maneja Claude). Definir cuál
  manda, o cómo sincronizarlas — el export/import JSON de la app es un
  punto de partida natural, casa con lo que ya pide la Fase 3.
- Evaluar si conviene que la app lea/escriba directo `coleccion.db` (con
  backend) en vez de duplicar el estado en `localStorage`.

## Fuera de alcance por ahora

- Integración de compra/venta automatizada, scraping de marketplaces, o
  cualquier cosa que dependa de credenciales de terceros — el skill asiste
  la decisión, Ana sigue comprando a mano.
