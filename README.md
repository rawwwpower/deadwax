# deadwax

App simple para llevar tu colección de discos y tu wantlist, pensada para usar
desde el celular en la disquería.

## Uso

Abrí `index.html` en el navegador (o serví la carpeta con cualquier servidor
estático). Todo se guarda en el navegador (`localStorage`), no requiere
backend ni conexión.

- **Colección**: los discos que ya tenés.
- **Wantlist**: los que buscás. Botón "Comprado" los pasa directo a tu
  colección.
- **Exportar/Importar**: backup en JSON, abajo de todo.

## Escalar a futuro

La lógica de guardado vive toda en el objeto `Store` de `js/app.js`
(`getAll`, `saveAll`, `upsert`, `remove`). Para pasar a un backend real
(sync entre dispositivos, compartir colección, etc.) alcanza con reemplazar
esos métodos por llamadas a una API, sin tocar el resto de la UI.
