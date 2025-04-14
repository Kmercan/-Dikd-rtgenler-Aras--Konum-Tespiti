import sqlite3
import random

db=sqlite3.connect("veritabani.db")
imlec=db.cursor()


imlec.execute('''CREATE TABLE IF NOT EXISTS cizgi
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              x1 INT , y1 INT , x2 INT , y2 INT)''')

kayitSayisi=0

while kayitSayisi < 100:
    x1=random.randint(1,1000)
    y1=random.randint(1,1000)
    x2=random.randint(1,1000)
    y2=random.randint(1,1000)
  

    if x1 < x2 and (x2-x1) <=100 and y1 < y2 and (y2-y1)<=100:
        imlec.execute('INSERT INTO cizgi(x1,y1,x2,y2) VALUES (?,?,?,?)',(x1,y1,x2,y2))
        kayitSayisi+=1

db.commit()
db.close()