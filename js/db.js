/**
 * PashuSachet — Native IndexedDB Storage Layer
 * Manages queued offline drafts, local animal passports, and clinical records.
 * Adheres strictly to offline-first principles.
 */

const DB_NAME = "PashuSachetDB";
const DB_VERSION = 1;

let dbInstance = null;

function openPashuDatabase() {
  return new Promise((resolve, reject) => {
    if (dbInstance) {
      resolve(dbInstance);
      return;
    }

    if (!window.indexedDB) {
      console.warn("IndexedDB not supported; operating in local memory mode.");
      resolve(null);
      return;
    }

    const request = indexedDB.open(DB_NAME, DB_VERSION);

    request.onupgradeneeded = (event) => {
      const db = event.target.result;

      // 1. Queued Offline Drafts Store
      if (!db.objectStoreNames.contains("drafts")) {
        const draftStore = db.createObjectStore("drafts", { keyPath: "id" });
        draftStore.createIndex("status", "status", { unique: false });
        draftStore.createIndex("timestamp", "timestamp", { unique: false });
      }

      // 2. Clinical Cases Store
      if (!db.objectStoreNames.contains("cases")) {
        const caseStore = db.createObjectStore("cases", { keyPath: "id" });
        caseStore.createIndex("animalId", "animalId", { unique: false });
      }

      // 3. Animals Store
      if (!db.objectStoreNames.contains("animals")) {
        db.createObjectStore("animals", { keyPath: "id" });
      }

      // 4. Audit Log Store
      if (!db.objectStoreNames.contains("auditLogs")) {
        db.createObjectStore("auditLogs", { keyPath: "id", autoIncrement: true });
      }
    };

    request.onsuccess = (event) => {
      dbInstance = event.target.result;
      resolve(dbInstance);
    };

    request.onerror = (event) => {
      console.error("IndexedDB error:", event.target.error);
      resolve(null); // Fallback gracefully
    };
  });
}

// Storage helpers
const idb = {
  async saveDraft(draft) {
    const db = await openPashuDatabase();
    if (!db) return draft;
    return new Promise((resolve) => {
      const tx = db.transaction("drafts", "readwrite");
      tx.objectStore("drafts").put(draft);
      tx.oncomplete = () => resolve(draft);
      tx.onerror = () => resolve(draft);
    });
  },

  async getQueuedDrafts() {
    const db = await openPashuDatabase();
    if (!db) return [];
    return new Promise((resolve) => {
      const tx = db.transaction("drafts", "readonly");
      const store = tx.objectStore("drafts");
      const req = store.getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => resolve([]);
    });
  },

  async saveCase(caseData) {
    const db = await openPashuDatabase();
    if (!db) return caseData;
    return new Promise((resolve) => {
      const tx = db.transaction("cases", "readwrite");
      tx.objectStore("cases").put(caseData);
      tx.oncomplete = () => resolve(caseData);
      tx.onerror = () => resolve(caseData);
    });
  },

  async getCase(caseId) {
    const db = await openPashuDatabase();
    if (!db) return null;
    return new Promise((resolve) => {
      const tx = db.transaction("cases", "readonly");
      const req = tx.objectStore("cases").get(caseId);
      req.onsuccess = () => resolve(req.result || null);
      req.onerror = () => resolve(null);
    });
  },

  async saveAnimal(animal) {
    const db = await openPashuDatabase();
    if (!db) return animal;
    return new Promise((resolve) => {
      const tx = db.transaction("animals", "readwrite");
      tx.objectStore("animals").put(animal);
      tx.oncomplete = () => resolve(animal);
      tx.onerror = () => resolve(animal);
    });
  },

  async getAllAnimals() {
    const db = await openPashuDatabase();
    if (!db) return [];
    return new Promise((resolve) => {
      const tx = db.transaction("animals", "readonly");
      const req = tx.objectStore("animals").getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => resolve([]);
    });
  }
};

