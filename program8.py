import sqlite3
carData= [
    (1, 'Audi', 52642),
    (2, 'Mercedes', 52642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 35000),
    (6, 'citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 54906)
     ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("CREATE TABLE cars(Id INT,Name TEXT,price INT)")
cur.executemany("INSERT INTO cars values(?,?,?)",carData)
con.commit()
con.close()
print("values inserted.")
