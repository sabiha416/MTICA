import sqlite3 as lite
con = lite.connect('mtica.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute('''CREATE TABLE   cars(
        Id INT,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',52642)")



cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO cars VALUES(5,'Bentley',35000)")
cur.execute("INSERT INTO cars VALUES(6,'citroen',21000)")
cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',54906)")


con.commit()
print("values in table inserted.")
