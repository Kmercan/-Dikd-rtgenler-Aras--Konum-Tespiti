Bu proje, iki boyutlu uzayda rastgele oluşturulmuş 100 adet dikdörtgenin SQLite veritabanında saklanmasını ve bu dikdörtgenler arasındaki geometrik ilişkilerin analiz edilmesini amaçlamaktadır. Her dikdörtgen, iki köşe noktasının koordinatları (x1, y1) ve (x2, y2) ile tanımlanmakta olup, veritabanına uygun koşullarla (x1 ≤ x2, y1 ≤ y2, kenar uzunluğu ≤ 100) yerleştirilmektedir.

Proje kapsamında şu üç durum analiz edilmektedir:

Kesişme: İki dikdörtgenin ortak bir alana sahip olması.

Kapsama: Bir dikdörtgenin tamamen başka bir dikdörtgenin içinde kalması.

Temassızlık: Bir dikdörtgenin hiçbir diğer dikdörtgenle kesişmemesi.
