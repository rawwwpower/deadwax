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

- Alguna forma liviana de ver la colección sin pasar por el CLI (filtros por
  owner/status/sello/país, estadísticas). No está decidido si esto es una
  app separada, un dashboard estático generado del export, o algo dentro
  del propio repo.

## Fuera de alcance por ahora

- Integración de compra/venta automatizada, scraping de marketplaces, o
  cualquier cosa que dependa de credenciales de terceros — el skill asiste
  la decisión, Ana sigue comprando a mano.
