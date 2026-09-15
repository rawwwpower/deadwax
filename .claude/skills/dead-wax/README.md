# dead-wax (skill de Claude Code)

Este skill vive en `.claude/skills/dead-wax/` como parte del proyecto
[Dead Wax](../../../README.md). Claude Code lo detecta automáticamente al
abrir este repo (`SKILL.md` es el punto de entrada) — no hace falta
invocarlo a mano, se activa solo cuando la conversación toca vinilos,
prensados o la colección.

## Qué incluye

```
dead-wax/
├── SKILL.md                     ← metodología + reglas, lo que Claude lee al activar el skill
├── references/
│   ├── guia-completa.md         ← guía completa con los casos trabajados
│   ├── checklist-rapido.md      ← versión de bolsillo de los 3 filtros
│   └── casos-especificos.md     ← firmas de autenticación puntuales, bootlegs conocidos, notas regionales
├── scripts/
│   └── coleccion.py             ← CLI para leer/escribir la base de datos (sin dependencias, solo stdlib)
└── data/
    └── coleccion.db             ← SQLite con la colección: discos de `ana` y de `seba` (campo `owner`)
```

## Probarlo a mano (sin Claude, para verificar que la base anda)

```bash
cd .claude/skills/dead-wax
python3 scripts/coleccion.py list
python3 scripts/coleccion.py list --owner seba
python3 scripts/coleccion.py stats
python3 scripts/coleccion.py search "Sabbath"
```

## Cómo lo usa Claude en la práctica

Cuando le mandes una foto de un disco o le preguntes "¿vale la pena esto?",
el skill le dice que primero busque en `coleccion.db` (por si ya lo
evaluaste o ya lo tenés), después aplique los 3 criterios de
`SKILL.md`/`references/`, y al final, **solo si confirmás la compra**, lo
agregue con:

```bash
python3 scripts/coleccion.py add --artista "..." --titulo "..." --pais "..." \
  --sello "..." --catalogo "..." --anio 1975 --status owned
```

## Portabilidad

Esta carpeta es autocontenida (metodología + CLI + datos, sin dependencias
externas más allá de `sqlite3` de la stdlib), así que se puede copiar tal
cual a otro repo o a `~/.claude/skills/dead-wax/` para tenerla disponible en
todos lados. El resto del proyecto (ver [roadmap](../../../ROADMAP.md)) es
lo que no es portable: vive acá.
