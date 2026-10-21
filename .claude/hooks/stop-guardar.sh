#!/bin/bash
# Al terminar cada respuesta: si quedó algo sin commitear o sin pushear,
# no deja cerrar y le pide a Claude que lo guarde y deje el PR listo.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

input=$(cat)
# Si ya se frenó una vez en este turno, no insistir (evita loops).
if echo "$input" | grep -q '"stop_hook_active": *true'; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

sucio=$(git status --porcelain 2>/dev/null)
rama=$(git branch --show-current)
if git rev-parse -q --verify "origin/$rama" >/dev/null; then
  sin_push=$(git rev-list --count "origin/$rama..HEAD" 2>/dev/null || echo 0)
else
  sin_push=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
fi

if [ -z "$sucio" ] && [ "$sin_push" -eq 0 ]; then
  exit 0
fi

motivo="Hay trabajo de Dead Wax sin guardar (cambios sin commitear: $( [ -n "$sucio" ] && echo sí || echo no ); commits sin pushear: $sin_push). Antes de terminar: si cambió coleccion.db, regenerar js/seed-data.js y vinilos.html (y republicar el artifact); si se decidió o quedó algo abierto, anotarlo en EQUIPO.md o curaduria/PENDIENTES.md; respetar la Privacidad de SKILL.md; después commit, git push -u origin $rama y, si no hay un PR abierto para esta rama, abrir uno a main y pasarle el link a Ana para el Merge. Si algo no se debe guardar, decirlo en la respuesta."
printf '{"decision":"block","reason":%s}\n' "$(printf '%s' "$motivo" | python3 -c 'import json,sys;print(json.dumps(sys.stdin.read()))')"
exit 0
