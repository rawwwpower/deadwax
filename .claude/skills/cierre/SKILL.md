---
name: cierre
description: Cierre de sesión de Dead Wax. Anota el punto de retome en curaduria/PENDIENTES.md (o EQUIPO.md si fue de equipo/mezcla), guarda lo que tiene que sobrevivir entre sesiones, regenera las salidas si cambió la base, commitea, pushea, deja el PR a main listo y le devuelve a Ana la frase para abrir la próxima. Usar cuando Ana escribe /cierre, "cerremos", "cierro acá", "seguimos en otra sesión" o similar.
---

# /cierre

Ana cierra las sesiones así para arrancar otra con el contexto intacto. La próxima sesión no ve esta conversación:
tiene que poder retomar sin preguntarle nada.

## 1. Juntar qué pasó en esta sesión

Repasá la conversación y separá:
- **Decidido:** lo que Ana eligió, descartó o corrigió (con su criterio, no sólo el resultado). Sus correcciones valen más
  que tus propuestas.
- **Abierto:** lo que quedó esperando a Ana, a Seba o a un vendedor/tienda (decí a quién).
- **Dónde está:** archivos, ids de la base (`coleccion.py show <id>`), catálogos, links de anuncios o artifacts.
- **Datos nuevos:** ediciones identificadas, precios de referencia, reviews de sonido, datos de equipo.

Si la sesión no tuvo nada para guardar, decilo en una línea y no toques archivos.

## 2. Punto de retome

- **Curaduría, compras, colección:** en `.claude/skills/dead-wax/curaduria/PENDIENTES.md`, agregá una sección nueva arriba de
  todo, justo debajo del párrafo de introducción, con el formato
  `## Retomar acá (<d mmm aaaa>, <momento>): <de qué se trata, corto>` y un párrafo denso (≈120 caracteres por línea) con lo
  decidido, las rutas/ids en **negrita con backticks**, lo descartado y lo abierto. Si un ítem de "Abierto" se resolvió,
  sacalo o actualizalo ahí mismo. No reescribas ni borres las otras secciones.
- **Equipo y mezcla:** lo mismo en `EQUIPO.md` (decisiones, compras, lo que falta probar).
- **App / skill / repo:** si quedó trabajo de código a medias, `ROADMAP.md` o una línea en PENDIENTES.md.

## 3. Lo que tiene que sobrevivir (el "contexto compartido" de este proyecto)

Con edición puntual, nunca reescribiendo el archivo entero:
- **Gustos o criterios nuevos de Ana o Seba** (un disco que les encantó, un género que no va, cómo priorizar): sección
  "Gustos de Ana y Seba" de `.claude/skills/dead-wax/SKILL.md`, viñeta con fecha.
- **Feedback sobre cómo trabajar** (formato de respuesta, qué no repetir): "Estilo al responder" de `SKILL.md`, o
  `CLAUDE.md` si aplica a todo el repo. Revisá antes que no exista ya.
- Si algo contradice una entrada anterior, decí que la reemplaza ("PISA lo anterior").

## 4. Salidas generadas

Si cambió `data/coleccion.db` en esta sesión:
```
python3 scripts/export-coleccion-a-app.py
python3 .claude/skills/dead-wax/curaduria/vinilos/build.py
```
y republicá `vinilos.html` en el artifact de siempre (https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5).

## 5. Privacidad (el repo es público)

Antes de commitear, releé el diff: nada de email, apellido, dónde vive, lo que pagó por discos propios ni frases sobre el
valor de la colección (detalle en "Privacidad" de `.claude/skills/dead-wax/SKILL.md`). Nombres de terceros, sólo el nombre de
pila o el de la tienda.

## 6. Commit, push y PR

- Commiteá sólo los archivos que tocó esta sesión. Si hay otros cambios que no son tuyos, no los sumes y avisá en una línea.
- Mensaje en español, con el estilo del log (`git log --oneline -5`): `<área>: <qué cambió>`.
- **Push siempre** (el contenedor se borra; lo que no se pushea se pierde): `git push -u origin <rama>`.
- Si no hay un PR abierto de esta rama, abrí uno a `main`; si ya hay, el push lo actualiza. El merge lo hace Ana a mano
  (decisión del 21/10/2026): no mergear.

## 7. Respuesta a Ana

Corta, sin repetir todo lo guardado:
- Tres viñetas como máximo: qué quedó guardado y dónde, qué quedó abierto y para quién, y el commit + link del PR (o que
  no hubo).
- Si se republicó un artifact, su link (regla de `CLAUDE.md`).
- Después, en un bloque de código aparte, la frase para abrir la próxima sesión, lista para pegar, por ejemplo:
  `Retomemos Dead Wax: leé "Retomar acá (21 oct 2026, cierre)" en .claude/skills/dead-wax/curaduria/PENDIENTES.md y seguimos con <lo próximo>.`

Estilo: español rioplatense, sin guiones largos ni em dashes, fechas absolutas (nunca "hoy" ni "ayer" en lo guardado).
