// Storage layer: swap this module for a backend-backed one later
// without touching the UI code below.
const Store = {
  KEY: "deadwax_records",

  getAll() {
    try {
      return JSON.parse(localStorage.getItem(this.KEY)) || [];
    } catch {
      return [];
    }
  },

  saveAll(records) {
    localStorage.setItem(this.KEY, JSON.stringify(records));
  },

  upsert(record) {
    const all = this.getAll();
    const idx = all.findIndex((r) => r.id === record.id);
    if (idx === -1) all.push(record);
    else all[idx] = record;
    this.saveAll(all);
  },

  remove(id) {
    this.saveAll(this.getAll().filter((r) => r.id !== id));
  },
};

const state = {
  tab: "collection",
  query: "",
};

const listEl = document.getElementById("list");
const emptyEl = document.getElementById("empty");
const searchEl = document.getElementById("search");
const dialogEl = document.getElementById("record-dialog");
const formEl = document.getElementById("record-form");
const deleteBtn = document.getElementById("delete-btn");

document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    state.tab = btn.dataset.tab;
    render();
  });
});

searchEl.addEventListener("input", () => {
  state.query = searchEl.value.trim().toLowerCase();
  render();
});

function matchesQuery(record) {
  if (!state.query) return true;
  const haystack = `${record.artist} ${record.album} ${record.label || ""}`.toLowerCase();
  return haystack.includes(state.query);
}

function render() {
  const records = Store.getAll()
    .filter((r) => r.type === state.tab)
    .filter(matchesQuery)
    .sort((a, b) => a.artist.localeCompare(b.artist) || a.album.localeCompare(b.album));

  listEl.innerHTML = "";
  emptyEl.hidden = records.length > 0;
  emptyEl.textContent =
    state.tab === "collection"
      ? "Todavía no cargaste discos en tu colección."
      : "Tu wantlist está vacía.";

  for (const record of records) {
    listEl.appendChild(renderCard(record));
  }
}

function renderCard(record) {
  const card = document.createElement("div");
  card.className = "card";

  const main = document.createElement("div");
  main.className = "card-main";

  const title = document.createElement("div");
  title.className = "card-title";
  title.textContent = `${record.artist} — ${record.album}`;

  const sub = document.createElement("div");
  sub.className = "card-sub";
  sub.textContent = [record.label, record.year, record.format].filter(Boolean).join(" · ");

  main.append(title, sub);
  card.appendChild(main);

  const actions = document.createElement("div");
  actions.className = "card-actions";

  if (record.type === "wantlist") {
    const buyBtn = document.createElement("button");
    buyBtn.className = "pill-btn buy";
    buyBtn.textContent = "Comprado";
    buyBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      markAsPurchased(record);
    });
    actions.appendChild(buyBtn);
  }

  card.appendChild(actions);
  card.addEventListener("click", () => openDialog(record));
  return card;
}

function markAsPurchased(record) {
  Store.remove(record.id);
  Store.upsert({ ...record, type: "collection", id: crypto.randomUUID() });
  render();
}

function openDialog(record) {
  document.getElementById("dialog-title").textContent = record
    ? "Editar disco"
    : `Nuevo disco — ${state.tab === "collection" ? "Colección" : "Wantlist"}`;
  document.getElementById("record-id").value = record ? record.id : "";
  document.getElementById("record-type").value = record ? record.type : state.tab;
  document.getElementById("f-artist").value = record ? record.artist : "";
  document.getElementById("f-album").value = record ? record.album : "";
  document.getElementById("f-label").value = record ? record.label || "" : "";
  document.getElementById("f-year").value = record ? record.year || "" : "";
  document.getElementById("f-format").value = record ? record.format || "LP" : "LP";
  document.getElementById("f-notes").value = record ? record.notes || "" : "";
  deleteBtn.hidden = !record;
  dialogEl.showModal();
}

document.getElementById("fab").addEventListener("click", () => openDialog(null));
document.getElementById("cancel-btn").addEventListener("click", () => dialogEl.close());

deleteBtn.addEventListener("click", () => {
  const id = document.getElementById("record-id").value;
  if (id) Store.remove(id);
  dialogEl.close();
  render();
});

formEl.addEventListener("submit", () => {
  const id = document.getElementById("record-id").value || crypto.randomUUID();
  const record = {
    id,
    type: document.getElementById("record-type").value,
    artist: document.getElementById("f-artist").value.trim(),
    album: document.getElementById("f-album").value.trim(),
    label: document.getElementById("f-label").value.trim(),
    year: document.getElementById("f-year").value.trim(),
    format: document.getElementById("f-format").value,
    notes: document.getElementById("f-notes").value.trim(),
  };
  if (!record.artist || !record.album) return;
  Store.upsert(record);
  render();
});

document.getElementById("export-btn").addEventListener("click", () => {
  const blob = new Blob([JSON.stringify(Store.getAll(), null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `deadwax-backup-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
});

document.getElementById("import-input").addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  try {
    const imported = JSON.parse(await file.text());
    if (!Array.isArray(imported)) throw new Error("invalid format");
    const existing = Store.getAll();
    const byId = new Map(existing.map((r) => [r.id, r]));
    for (const r of imported) byId.set(r.id, r);
    Store.saveAll([...byId.values()]);
    render();
  } catch {
    alert("No se pudo importar el archivo. ¿Es un backup de deadwax en formato JSON?");
  } finally {
    e.target.value = "";
  }
});

render();
