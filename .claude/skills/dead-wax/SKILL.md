---
name: dead-wax
description: Metodología de Ana para evaluar y catalogar ediciones de vinilo (autenticación de prensados, tres criterios de evaluación, jerarquía de plantas, red flags de sellos truchos) y para consultar/actualizar su colección personal "Dead Wax" en la base de datos local. Usar SIEMPRE que se mencione un disco de vinilo, un anuncio de venta, una foto de tapa/etiqueta/dead wax, un catálogo de Discogs, o cualquier pregunta tipo "¿vale la pena este vinilo?", "¿es original?", "¿qué prensado es mejor?", aunque no se use la palabra "skill" o "colección" explícitamente. También usar para cualquier consulta sobre qué discos tiene Ana, agregar un disco nuevo, o buscar en su inventario.
---

# Dead Wax — evaluación y catálogo de vinilos

Este skill tiene dos partes que casi siempre van juntas:

1. **La metodología** (cómo juzgar si una edición puntual vale la pena) — está resumida acá abajo, con el detalle completo en `references/`.
2. **La base de datos de la colección** — un SQLite local en `data/coleccion.db`, manejado con `scripts/coleccion.py`. Es la fuente de verdad de qué discos tiene Ana, cuáles evaluó y no compró, y qué queda pendiente.

## Regla de oro antes de arrancar

Nunca evalúes de memoria ni por similitud. Siempre:
- Pedí o extraé el **catálogo completo exacto** tal cual aparece en la foto (contratapa, etiqueta, lomo) — no asumas país/edición por parecido con otra que conocés.
- Comparalo contra el **master de Discogs** para ese álbum, ubicando la edición exacta entre las versiones listadas.
- Si hay foto de dead wax/matrix, usala para confirmar la prensa exacta (ver vocabulario abajo).

## Los tres criterios (resumen — detalle en `references/guia-completa.md`)

1. **¿Es de época o reedición?** Prensa contemporánea al lanzamiento > reedición moderna, salvo sello audiófilo reconocido (Analogue Productions, Speakers Corner, Sundazed, Classic Records, RhinOvinyl) sobre un original inconseguible o sonoramente superado.
2. **¿Es del país/sello de origen, o licencia local?** La licencia local puede ser legítima (chequear si el sello tenía licencia oficial, ej. Microfón-Island, CBS Argentina-CBS internacional) pero no es "la fuente".
3. **¿Qué tan buena es la planta/mercado?** Jerarquía general (no absoluta, varía por título):

   **Japón > UK/Europa (Alemania, Países Bajos) > USA/Brasil > Argentina y licencias locales 70s-80s > sellos truchos**

## Red flags 🚩 y sellos de mala fama

Tapa simple donde debería ser gatefold, sin datos de fabricación/distribuidora impresos, catálogo de tapa que no coincide con el de etiqueta → sospechar reedición trucha/bootleg.

Lista negra: DOL, Doxy, ZYX, Vinyl Lovers, Simply Vinyl, Abraxas, Tapestry, ABKCO (en algunas reediciones), Friday Music (variable), Get Back, Vinyl Magic, Lilith, Akarma, Not Now Music, Vinyl Passion.

Mobile Fidelity (MoFi): buena fama pero con el antecedente del escándalo 2022 (paso digital DSD en discos vendidos como "all-analog").

## Vocabulario clave

- **Matrix / runout / dead wax**: código grabado o estampado en los surcos sin música, cerca de la etiqueta. Compararlo contra Discogs confirma la edición exacta. Grabado a mano (etching) = señal de prensa genuina; etchings genéricos o ausentes en algo que debería tenerlos = sospechoso.
- **Obi**: faja de papel japonesa en el lomo. Si falta no descalifica, pero baja el valor de colección.
- **Promo**: copia para radio/prensa ("muestra sin valor comercial"). Más rara, no necesariamente mejor sonido.
- **Grading (Goldmine)**: M > NM > VG+ > VG > G > P. Se gradúa disco y tapa por separado (ej. "NM/VG+"). VG+ ronda el 50% del valor de una NM.
- **Copia casada (married copy)**: disco y tapa que no son de la misma edición original. Baja valor de colección, no afecta sonido — buen argumento de negociación de precio.

## Workflow para evaluar un hallazgo

1. Extraer artista, título, catálogo, sello, país, año del anuncio/foto.
2. Buscar primero en la propia colección: `python scripts/coleccion.py search "<catálogo o artista>"` — puede que ya lo tenga o ya lo haya evaluado antes.
3. Buscar el master en Discogs, ubicar la edición exacta.
4. Leer reseñas de esa edición puntual (a veces comparan sonido entre ediciones o reportan defectos de prensado).
5. Aplicar los tres criterios + revisar contra la lista negra.
6. Chequear precio contra el histórico (Discogs stats o popsike.com) — la mediana es la referencia.
7. Dar veredicto directo (comprar / pasar / comprar solo si baja de precio) con la razón, sin hedgear de más.
8. **Evaluar no es lo mismo que comprar.** Solo loguear en la base como "owned" si Ana confirma explícitamente que lo compró o ya lo tiene. Una consulta tipo "¿vale la pena esto?" es evaluación pura: dar el veredicto y listo, **no preguntar si hay que cargarlo** ni cargarlo como `pendiente` por las dudas — eso genera ruido. Solo se carga algo (y ahí sí, sin volver a confirmar) cuando ella lo pide explícitamente ("sumalo", "cargalo", "ya lo tengo", "lo compré") o cuando ya está claro por contexto que es un disco que posee (ej. "está sonando en casa de Seba").

## Manejo de la base de datos

Ver `scripts/coleccion.py` para el detalle de comandos (`add`, `search`, `list`, `stats`). Reglas:

- Todo disco que Ana confirme como comprado o ya tenido va con `status=owned`.
- Todo disco evaluado pero no comprado va con `status=evaluado_no_comprado` (para no re-evaluar de cero si vuelve a aparecer).
- Todo disco identificado como pendiente de investigar más (falta matrix, falta confirmar edición) va con `status=pendiente`.
- Siempre guardar el catálogo exacto y, si existe, el Discogs release ID — son la clave para no confundir ediciones parecidas.
- **Campo `owner`**: la base guarda dos colecciones separadas, `ana` (default) y `seba` — comparten sesiones de escucha pero son colecciones distintas de cada uno. Nunca asumir que un disco es de Ana si no se aclara; si Ana menciona algo de Seba (o viceversa), usar `--owner seba` explícitamente. Al buscar o listar, tener en cuenta que puede haber resultados de ambos dueños.
- **Datos faltantes (país/sello/catálogo)**: si al cargar un disco no hay foto de tapa/etiqueta con esos datos, cargarlo igual con lo que se sepa (status real: `owned` si ya está confirmado como propio, aunque falte identificar la edición exacta) y dejar esos campos vacíos. **No volver a pedir esa info en el momento** — se completa después, en rondas de repaso con Seba. Para armar esas rondas: `python3 scripts/coleccion.py list --incomplete` lista todo lo que tiene país, sello o catálogo vacío, de cualquier owner/status.
  - `status=pendiente` es solo para "no decidido si se compra" (afecta cómo lo lee la app: aparece en wantlist) — no usarlo para "ya lo tengo pero falta identificar la edición", eso es `owned` + campos vacíos.

## Estilo al responder

Español argentino, informal, directo. Sin guiones largos (—); usar comas, dos puntos o paréntesis. Veredictos claros, no hedgeados. Raw/Ana suele mandar fotos con poco texto: extraer e interpretar los detalles relevantes de la foto de forma autónoma.

**Siempre que la respuesta venga de una búsqueda** (Discogs, precios, identificación de edición, trivia, lo que sea), cerrar con las keywords/queries exactas usadas — así ella puede repetir la búsqueda por su cuenta con la misma precisión, sin que se lo tenga que pedir cada vez.

## Archivos de referencia

- `references/guia-completa.md` — guía completa con casos trabajados (Sumo, Grace Jones, Black Sabbath, AC/DC, Talking Heads) para consultar cuando un caso es ambiguo o parecido a uno ya resuelto.
- `references/checklist-rapido.md` — versión de bolsillo de los 3 filtros, para chequear parado frente al anuncio.
- `references/casos-especificos.md` — firmas de autenticación puntuales (PORKY/PECKO en Vertigo UK, locked groove en Slayer *Reign in Blood*), bootlegs conocidos por catálogo exacto, y notas regionales/de marketing aprendidas caso por caso. **Consultar siempre que el disco en cuestión sea Vertigo UK, Slayer *Reign in Blood*, Goblin *Profondo Rosso*, o cualquier reedición sospechosa de "loudness war".**
