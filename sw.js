/* Service worker de « Les Tables Magiques ».
   Rend l'application installable et utilisable hors connexion.
   Bumper VERSION a chaque mise en ligne pour forcer le rafraichissement. */
const VERSION = 'v1';
const CACHE = 'tables-magiques-' + VERSION;

// Chemins relatifs au scope : fonctionne aussi sous /nom-du-depot/
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon-32.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => c.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(noms => Promise.all(noms.filter(n => n !== CACHE).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if(req.method !== 'GET') return;

  // Navigation : reseau d'abord (pour recuperer les mises a jour), cache en secours
  if(req.mode === 'navigate'){
    e.respondWith(
      fetch(req)
        .then(rep => { majCache(req, rep.clone()); return rep; })
        .catch(() => caches.match(req).then(r => r || caches.match('./index.html')))
    );
    return;
  }

  // Reste (icones, polices) : cache d'abord, puis reseau
  e.respondWith(
    caches.match(req).then(hit => hit || fetch(req).then(rep => {
      if(rep && (rep.ok || rep.type === 'opaque')) majCache(req, rep.clone());
      return rep;
    }))
  );
});

function majCache(req, rep){
  caches.open(CACHE).then(c => c.put(req, rep)).catch(() => {});
}
