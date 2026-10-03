# vinilos (la página)

Colección + wishlist + buscador, publicada como artifact en
https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5 (privado; Ana la comparte desde Share).

**Se genera desde `data/coleccion.db`. No editar `vinilos.html` a mano.**

| Archivo | Qué es |
|---|---|
| `build.py` | Lee la base y arma `vinilos.html` (colección = `owned`; wishlist = discos con `prioridad`). |
| `template.html` | La página sin datos. Estilo de anavare.la: fondo `#1c1c1a`, Switzer + Geist Mono, grises zinc, minúsculas. |
| `fonts.css` | Las fuentes embebidas (la página no carga nada externo: tiene que ser liviana). |
| `mb.py` → `mbids.json` | Busca en MusicBrainz el release-group de cada disco (solo los que faltan). |
| `covers.py` → `covers.json` | Baja las tapas como JPEG 88×88 embebido. |
| `vinilos.html` | El resultado, lo que se publica. |

## Flujo

```
python3 mb.py && python3 covers.py   # solo si entraron discos nuevos
python3 build.py
```

Después, republicar `vinilos.html` con la tool Artifact pasando el `url` de arriba (si no, sale otro link).

## Tapas: cosas aprendidas

- **Revisar las tapas nuevas a ojo** (armar una hoja de contactos). `mb.py` busca el álbum por defecto,
  porque MusicBrainz a veces devuelve el simple homónimo y su tapa (pasó con Back in Black, Toxicity,
  Sweet Dreams). Los que sí son simples/maxis van en `TIPO` dentro de `mb.py`.
- Si la miniatura del grupo no es la tapa (ej. muestra la etiqueta), en `mbids.json` se puede poner
  `"release:<id>"` para forzar un release puntual, y re-bajar con `python3 covers.py "Artista | Título"`.
  Para no buscar nada (bootlegs, discos que no están en MusicBrainz), poner `null`: queda con las iniciales.
- Los nodos `dnXXXXXX.ca.archive.org` / `iaXXX.us.archive.org` están bloqueados por el proxy del sandbox.
  `covers.py` toma el identificador del item de la redirección de Cover Art Archive y baja
  `archive.org/services/img/<item>` (miniatura de ~180 px, servida directo).
- Para MusicBrainz, `MB_CONTACT` puede llevar el mail alternativo de Ana para el User-Agent, nunca el principal.
