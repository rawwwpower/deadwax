# Curaduría en curso

Estado al 03/10/2026, para retomar en una sesión nueva sin perder nada.
Leer esto antes de seguir con cualquier compra, carga a la base o la página de vinilos.

## Dónde vive cada cosa

- **Todo disco (tenido o querido) está en `data/coleccion.db`.** Colección = `status=owned`; wishlist =
  discos con `prioridad` (`top` / `interesante` / `evitar`), con `resumen`, `etiquetas` y `fuente`.
  Desde el 03/10/2026 ahí está también lo que antes vivía en tablas sueltas (la feria, los elegidos de
  Javierfan, los buscados), así que no hay que mantener listas aparte.
- **La página "vinilos"** (https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5) se genera desde la base:
  ver `vinilos/README.md`. Formato pedido por Ana: un renglón por disco, escaneable, con toda la info
  (edición, estado disco/tapa, alertas, el porqué completo, precio en pesos y USD a $1.600), y liviana
  (nada externo; tapas embebidas).
- Fuentes crudas: `feria-2026-09/lista-proveedor.txt` (561 ítems de la feria) y
  `javierfan-2026-09/catalogo-web.json` (catálogo de la web con stock; en MercadoLibre, JAVIERFAN1,
  los mismos discos salen ~8-12% más caros: comprar por la web).

## Abierto

- **AC/DC · Back in Black** (owned, id 41): confirmar cuál de las 8 variantes alemanas, con foto de
  etiqueta y dead wax.
- **Walter Carlos · Electronic Bach** (owned, id 51): falta la edición (país, sello, catálogo).
- **Aerosmith · Rocks** (wishlist): falta precio y si tiene obi.
- `coleccion.py list --incomplete` para la próxima ronda de repaso con Seba.
- Tapas que faltan (quedan con iniciales): Milton *Paixão e Fé*, Schoener *Video Magic*, Favio
  *Nazareno Cruz y el Lobo*, *Orange Mécanique*, Lennon *Shaved Fish*, Divine, Jack de Mello,
  Mister Sam, Elvis *Elvis Presley*, White Album y los bootlegs. No están (o no bien) en MusicBrainz.

## Hecho

- 27/09: página de la feria con tapas embebidas.
- 03/10: compras en Javierfan cargadas (Dirty Deeds, Sweet Dreams, Musiquarium, maxi de Kravitz).
  Siguen en la wishlist Bowie *Station to Station*, Hawkwind *Hall of the Mountain Grill* y Marley
  *Rastaman Vibration*.
- 03/10: la página pasa a ser "vinilos": colección + wishlist + buscador, generada desde la base.
