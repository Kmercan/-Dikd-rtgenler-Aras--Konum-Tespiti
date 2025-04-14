import sqlite3

db = sqlite3.connect("veritabani.db")
imlec = db.cursor()

imlec.execute("SELECT * FROM cizgi")
veriler = imlec.fetchall()

for id1, x1, y1, x2, y2 in veriler:
    kesisti_mi = False 

    for id2, a1, b1, a2, b2 in veriler:
        if id1 == id2:
            continue  

        if  (x2 >= a1 and x1 <=a2 and y2>=b1 and y1 <=b2):
            print(f"{id1} id'li ({x1},{y1})-({x2},{y2}) dikdörtgeni ile {id2} id'li ({a1},{b1})-({a2},{b2}) dikdörtgeni kesişiyor.")
            kesisti_mi = True

        if (a1 <= x1 and a2 >= x2 and b1 <= y1 and b2 >= y2):
            print(f"{id1} id'li ({x1},{y1})-({x2},{y2}) dikdörtgeni {id2} id'li ({a1},{b1})-({a2},{b2}) dikdörtgeni tarafından kapsanıyor.")
            kesisti_mi = True
    
    if not kesisti_mi:
        print(f"{id1}id’li dikdörtgen hiçbir dikdörtgen ile temas etmemektedir")

db.close()