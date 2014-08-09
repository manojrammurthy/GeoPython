import sqlite3
db = sqlite3.connect('data/mydb')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE geoadd(id INTEGER PRIMARY KEY, city TEXT,
                       pincode TEXT, country)
''')
db.commit()

cursor = db.cursor()
geoaddress = [(city,pincode,country)]
