# Discos consultados (no comprados)

Tabla de research en curso — discos que Ana evaluó pero todavía no compró.
Fuente cruda: `coleccion.py list --status pendiente` en `data/coleccion.db`
(campo `prensado_notas` de cada uno tiene el detalle completo con
catálogos/barcodes). Esta tabla es la síntesis visual, ordenada de más a
menos "sweet spot" (sonido + época + colección a la vez).

**Última actualización:** 2026-09-18

| # | Álbum | Edición recomendada | Sonido | Época | Colección | Por qué |
|---|---|---|---|---|---|---|
| 1 | **Madonna — Music** | Original 2000, Maverick/Warner, Alemania (cat. 9362-47865-1, barcode 093624786511) — **confirmada en Maniac Records, comprar** | ✅ Mismo máster que la reedición, mejor consistencia de prensado | ✅ Original de época | ✅ Typo "SDIE TWO" en la etiqueta para autenticar | Las 3 en una. Sweet spot real. |
| 2 | **Massive Attack — Mezzanine** | Reedición 2023, Alemania (barcode 602537540433) — **confirmada en Maniac Records, comprar** | ✅ Cortada en Metropolis Mastering, mismo estudio que el original | ⚠️ No es de época (el original 1998 es "el" sonido de referencia para puristas si aparece en buen estado) | ➖ Reedición común, no rara | Casi sweet spot — le falta la pata de época. |
| 3 | **Alice In Chains — Facelift** | Reedición 2020, Sony Legacy (barcode 194397838619) — **confirmada en Maniac Records, comprar** | ✅ Cortada por Chris Bellman, remasterizada en Gateway Mastering (estudio de Bob Ludwig) | ❌ Reedición 30° aniversario | ➖ No es rara | Sólida para sonido, no aporta época ni colección. |
| 4 | **The Chemical Brothers — Dig Your Own Hole** | Reedición 2016 gatefold (Mike Marsh, ingeniero original, aprobada por la banda) — **buscar esta, no la que ya encontró** | ✅ Mismo ingeniero que el original | ❌ No es de época | ➖ | La original 1997 (incluida la copia US Astralwerks cat. 4384295011 / barcode 724384295011 que encontró) tiene riesgo de distorsión — no vale sacrificar sonido por época acá. |
| 5 | **Fatboy Slim — You've Come a Long Way, Baby** | Half Speed Master Abbey Road: UK cat. BRASS11HSLP / barcode 4050538919004, o US Astralwerks RSD Essential cat. 602455862242 — **difícil de conseguir desde Argentina** | ✅ Abbey Road half-speed | ❌ | ✅ Tirada limitada (1.500-3.000 copias) | Sonido y colección altos, pero la logística de conseguirla la baja de puesto. Evitar la 2018 "Art of the Album" deluxe (BMGAA06LP / barcode 602567341390, la de Maniac Records) — reviews de sonido plano. |
| 6 | **Moby — Play** | Sin confirmar — buscar prensa en Optimal Media (Alemania): 2016 180g (Discogs r8465720) o 2022 140g (r24322403) | ⚠️ Depende de la planta; evitar el 2022 180g STUMM172 (Francia, r25028983) por ingeniero de corte inconsistente entre copias | — | — | La copia "Little Idiot 2022, 19 temas" que encontró no cierra contra Discogs (el STUMM172 francés tiene 18 temas) — pedirle foto/barcode antes de comprar. |
| 7 | **Divine — Love Reaction** (7") | Copia alemana ya encontrada, cat. 813 821-7 ME (Bob Cat / Metronome) | ➖ No aplica (7" pop, no es búsqueda audiófila) | ✅ Original 1983 | ➖ Común, no pagar más de US$10-12 | Más un capricho/anécdota (interpola el bajo de "Blue Monday" de New Order) que una compra "seria". Ana lo está viendo, no confirmó compra. |

## Cómo actualizar esta tabla

Cada vez que se evalúe un disco nuevo (o se confirme/descarte una edición
puntual), agregar la fila acá a mano y el registro correspondiente en
`coleccion.db` con `coleccion.py add ... --status pendiente`. Cuando algo
se compre, actualizar su `status` a `owned` (`coleccion.py update <id>
--status owned`) y sacarlo de esta tabla.
