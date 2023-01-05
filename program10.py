import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute('''
DELETE FROM Cars
WHERE Name='Sabiha'
''')
con.commit()
con.close()
print("Data Deleted")
     
