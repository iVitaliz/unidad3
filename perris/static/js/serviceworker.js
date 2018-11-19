var staticCacheName = 'djangopwa-v1';

var filesToCache = [
  '/',
  '/inicio.html',
  '/css/estilos.css',
  '/perris/static/img/adoptados/Tom',
  '/perris/static/img/adoptados/Duque',
  '/perris/static/img/adoptados/Apolo',
  '/perris/static/img/Rescate',
  '/perris/static/img/crowfunding',
  '/perris/static/img/rescatados/Oso',
  '/perris/static/img/rescatados/Oso_tn',
  '/perris/static/img/rescatados/Wifi',
  '/perris/static/img/rescatados/Wifi_tn',
  '/perris/static/img/rescatados/Rusia',
  '/perris/static/img/rescatados/Pexel',
  '/perris/static/img/rescatados/Pexel_tn',
  '/perris/static/img/rescatados/Maya',
  '/perris/static/img/rescatados/Maya_tn',
  '/perris/static/img/rescatados/Luna',
  '/perris/static/img/rescatados/Luna_tn',
  '/perris/static/img/rescatados/Chocolate',
  '/perris/static/img/rescatados/Chocolate_tn',
  '/perris/static/img/rescatados/Bigotes',
  '/perris/static/img/rescatados/bigotes_tn',

  
];

self.addEventListener('install', function(e) {
  console.log('[ServiceWorker] Install');
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      console.log('[ServiceWorker] Caching app shell');
      return cache.addAll(filesToCache);
    })
  );
});


self.addEventListener('fetch', function(e) {
  console.log('[ServiceWorker] Fetch', e.request.url);
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});


self.addEventListener('activate', function(e) {
  console.log('[ServiceWorker] Activate');
  e.waitUntil(
    caches.keys().then(function(keyList) {
      return Promise.all(keyList.map(function(key) {
        if (key !== cacheName) {
          console.log('[ServiceWorker] Removing old cache', key);
          return caches.delete(key);
        }
      }));
    })
  );
  return self.clients.claim();
});

