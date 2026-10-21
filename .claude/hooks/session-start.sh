#!/bin/bash
# Al arrancar una sesión: trae lo último de main a la rama de la sesión y
# le da a Claude el contexto para retomar sin que Ana repita nada.
# Lo que se imprime acá entra como contexto de la sesión.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

echo "## Dead Wax: arranque de sesión"

if git fetch -q origin 2>/dev/null; then
  if git merge -q --no-edit origin/main >/dev/null 2>&1; then
    echo "- main al día: ya está mergeado en la rama $(git branch --show-current)."
  else
    git merge --abort 2>/dev/null
    echo "- ⚠️ main NO se pudo mergear solo (conflicto, seguramente coleccion.db)."
    echo "  Antes de tocar nada, mergear a mano siguiendo CLAUDE.md (coleccion.db fila por fila)."
  fi

  # Ramas claude/* con trabajo que todavía no llegó a main (PR sin mergear).
  sueltas=""
  for b in $(git branch -r --format='%(refname:short)' | grep '^origin/claude/' | grep -v '^origin/claude/nana-ipod$'); do
    n=$(git rev-list --count origin/main.."$b" 2>/dev/null || echo 0)
    [ "$n" -gt 0 ] && sueltas="$sueltas $b($n)"
  done
  if [ -n "$sueltas" ]; then
    echo "- Ramas con commits que todavía no están en main:$sueltas"
    echo "  Ver si tienen un PR esperando el Merge de Ana; si no, traer su trabajo (sin perder registros de la base)."
  fi
else
  echo "- No se pudo hacer fetch de origin: trabajar con lo que hay y avisarle a Ana."
fi

echo
echo "### Últimos cambios en main"
git log origin/main --no-merges -8 --format='- %ad %s' --date=format:'%d/%m' 2>/dev/null

echo
echo "### Para retomar"
echo "- Equipo y mezcla: EQUIPO.md · Curaduría y compras abiertas: .claude/skills/dead-wax/curaduria/PENDIENTES.md"
echo "- Al guardar trabajo: commit + push y PR a main (Ana aprieta Merge). El hook de Stop avisa si quedó algo sin guardar."
exit 0
