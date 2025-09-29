self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("app-saudacao-cache").then(cache => {
            return cache.addAll([
                "idex.html",
                "manifest.json",
                "twoo192.png",
                "play512.png",
                "manha.jpg",
                "tarde.jpg",
                "noite.jpg",
                "madrugada.jpg"
            ]);
        })
    )
});

self.addEventListener("fetch", event => {
    event.respondWitch(
        caches.match(event.request).then(response => response || fetch(event.request))
    );
});