# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Two pieces sharing one SQLite database as source of truth:

1. **`.claude/skills/dead-wax/`** — a Claude Code skill: vinyl-pressing evaluation methodology (`SKILL.md` + `references/`) plus a CLI (`scripts/coleccion.py`) over `data/coleccion.db`. This is what lets Claude catalog/evaluate records when asked about vinyl — see `SKILL.md` for the full methodology and data-entry rules.
2. **Root (`index.html`, `css/`, `js/`)** — a static, client-side app (no backend) for browsing the collection/wantlist in a browser, storing state in `localStorage`.

The two do **not** share data live. `js/seed-data.js` is a generated snapshot of `coleccion.db` that the app loads once into `localStorage` on first run only (`seedIfNeeded()` in `js/app.js`, gated by a `deadwax_seeded` flag so it never overwrites what a viewer already added by hand). **Any time `coleccion.db` changes, regenerate and commit the seed:**

```
python3 scripts/export-coleccion-a-app.py   # rewrites js/seed-data.js from coleccion.db
```

This is a one-way, one-time sync (DB → app). There's no app → DB path yet (see `ROADMAP.md`, Fase 4).

## Commands

```
# Query/update the collection DB (the skill's CLI)
python3 .claude/skills/dead-wax/scripts/coleccion.py list [--owner ana|seba] [--status ...] [--incomplete]
python3 .claude/skills/dead-wax/scripts/coleccion.py add --artista "..." --titulo "..." --status owned ...
python3 .claude/skills/dead-wax/scripts/coleccion.py search "texto"
python3 .claude/skills/dead-wax/scripts/coleccion.py stats

# Regenerate the app's seed data after any DB change
python3 scripts/export-coleccion-a-app.py

# View the app — pure static, no build step
open index.html   # or serve the directory with any static file server
```

No build, lint, or test tooling in this repo: it's a stdlib-only Python CLI plus vanilla JS/HTML/CSS.

## Data model conventions (`data/coleccion.db`, table `discos`)

- `owner`: `ana` (default) or `seba` — two separate personal collections. Never assume a record is Ana's without it being said; infer/ask explicitly.
- `status`: `owned` / `evaluado_no_comprado` / `pendiente`. `pendiente` means "not decided whether to buy" (the export script maps it to the app's *wantlist*) — it is **not** for "owned but missing catalog/label/country data". A confirmed-owned record with an unidentified edition stays `status=owned` with those fields empty.
- Missing país/sello/catálogo at add-time: fill in what's known, leave the rest empty, don't ask again in the moment. `coleccion.py list --incomplete` surfaces every record with a gap, for periodic review rounds (see `SKILL.md`).

## Environment note (this sandbox specifically)

`git push origin --delete <branch>` gets rejected with a proxy-level 403 in this remote execution environment, regardless of which branch — deleting a remote branch has to be done by the repo owner in the GitHub UI. Likewise, changing the repo's default branch isn't reachable through any tool available here — that's a GitHub repo setting only the owner can change.

## Repo layout / roadmap

See `README.md` for the current split and `ROADMAP.md` for planned phases (offline Discogs indexing, bidirectional app↔DB sync, etc.) — the skill is deliberately scoped as one part of a larger project, not the whole thing.
