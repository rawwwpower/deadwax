# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Rol de Claude en este proyecto (pedido explícito de Ana)

Ana quiere que Claude sea **su ingeniera tech y de sonido**, no solo asistente
del catálogo: además de programar la app/skill, asesorar sobre equipo (bandejas,
cápsulas, mixer, pre, parlantes), calidad de audio de prensados y técnica.
Hablarle en castellano rioplatense.

Ana **quiere aprender a mezclar vinilos** (DJ). Su equipo actual, el plan de
compra y las decisiones tomadas viven en [`EQUIPO.md`](EQUIPO.md): leerlo antes
de responder cualquier cosa de equipo o mezcla, y actualizarlo cuando se decida
o se compre algo.

## Artifacts publicados (pedido de Ana)

Cada vez que se cambia algo de un artifact publicado (por ejemplo la wishlist de vinilos, https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5), terminar la respuesta con el link a ese artifact, aunque sea el mismo de siempre.

## What this repo is

Two pieces sharing one SQLite database as source of truth:

1. **`.claude/skills/dead-wax/`** — a Claude Code skill: vinyl-pressing evaluation methodology (`SKILL.md` + `references/`) plus a CLI (`scripts/coleccion.py`) over `data/coleccion.db`. This is what lets Claude catalog/evaluate records when asked about vinyl — see `SKILL.md` for the full methodology and data-entry rules.
2. **Root (`index.html`, `css/`, `js/`)** — a static, client-side app (no backend) for browsing the collection/wantlist in a browser, storing state in `localStorage`.

The two do **not** share data live. `js/seed-data.js` is a generated snapshot of `coleccion.db` that the app loads once into `localStorage` on first run only (`seedIfNeeded()` in `js/app.js`, gated by a `deadwax_seeded` flag so it never overwrites what a viewer already added by hand). **Any time `coleccion.db` changes, regenerate and commit the seed:**

```
python3 scripts/export-coleccion-a-app.py   # rewrites js/seed-data.js from coleccion.db
```

This is a one-way, one-time sync (DB → app).

The DB also feeds the **"vinilos" artifact** (collection + wishlist + search, `.claude/skills/dead-wax/curaduria/vinilos/`): `build.py` generates `vinilos.html` entirely from `coleccion.db` — never hand-edit it, and never keep a wishlist anywhere but the DB (`prioridad` column). There's no app → DB path yet (see `ROADMAP.md`, Fase 4).

## Commands

```
# Query/update the collection DB (the skill's CLI)
python3 .claude/skills/dead-wax/scripts/coleccion.py list [--owner ana|seba] [--status ...] [--incomplete]
python3 .claude/skills/dead-wax/scripts/coleccion.py add --artista "..." --titulo "..." --status owned ...
python3 .claude/skills/dead-wax/scripts/coleccion.py search "texto"
python3 .claude/skills/dead-wax/scripts/coleccion.py stats

# After any DB change: regenerate BOTH outputs
python3 scripts/export-coleccion-a-app.py                    # js/seed-data.js (the app)
python3 .claude/skills/dead-wax/curaduria/vinilos/build.py   # vinilos.html (the artifact; then republish it)

# View the app — pure static, no build step
open index.html   # or serve the directory with any static file server
```

No build, lint, or test tooling in this repo: it's a stdlib-only Python CLI plus vanilla JS/HTML/CSS.

## Data model conventions (`data/coleccion.db`, table `discos`)

- `owner`: `ana` (default) or `seba` — two separate personal collections. Never assume a record is Ana's without it being said; infer/ask explicitly.
- `status`: `owned` / `evaluado_no_comprado` / `pendiente` / `descubrimiento` (a record shown as a quick "ficha" for discovery, not a purchase evaluation).
- `review`: Ana's or Seba's own listening impressions, kept apart from the technical `notas`. `genero`: specific genre, filled for descubrimientos.
- `status` detail: `pendiente` means "not decided whether to buy" (the export script maps it to the app's *wantlist*) — it is **not** for "owned but missing catalog/label/country data". A confirmed-owned record with an unidentified edition stays `status=owned` with those fields empty.
- Missing país/sello/catálogo at add-time: fill in what's known, leave the rest empty, don't ask again in the moment. `coleccion.py list --incomplete` surfaces every record with a gap, for periodic review rounds (see `SKILL.md`).

## Branches: `main` is the only source of truth

Every Claude session works on its own `claude/...` branch. In Sep 2026 seven of these had piled up unmerged, with collection records living only on side branches. To keep that from happening again:

- **Start from `main`**: at the beginning of a session, merge the latest `origin/main` into the session branch before changing anything.
- **Close by opening a PR to `main`** whenever the session saved work (commit + push), and tell Ana it's waiting for her "Merge" click. A session's work isn't saved until it's in `main`.
- **`coleccion.db` is binary: git can't merge it.** On a conflict, never pick one side (records get lost). Merge row by row, keyed on `(owner, artista, titulo)`: union the columns and the rows, fill empty fields from the other side, and let `owned` win on `status`. Then regenerate `js/seed-data.js`.

## Environment note (this sandbox specifically)

`git push origin --delete <branch>` gets rejected with a proxy-level 403 in this remote execution environment, regardless of which branch — deleting a remote branch has to be done by the repo owner in the GitHub UI. Likewise, changing the repo's default branch isn't reachable through any tool available here — that's a GitHub repo setting only the owner can change.

## Repo layout / roadmap

See `README.md` for the current split and `ROADMAP.md` for planned phases (offline Discogs indexing, bidirectional app↔DB sync, etc.) — the skill is deliberately scoped as one part of a larger project, not the whole thing.
