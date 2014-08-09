import urllib
import json
import sqlite3

print "Enter the pincode of area that you want to see"
pincode = raw_input("> ")
print "Enter  the country name "
country = raw_input("> ")
url = "https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:"
url1 = url + pincode + "|country:" + country
#url = "https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:%d" % pincode
print  url1
jdata = urllib.urlopen(url1)
fp = json.load(jdata)
#print fp["results"]
city = json.dumps([s['address_components'][2]['long_name'] for s in fp['results']], indent=2)
print city
db = sqlite3.connect('mydb')
print "opened databaase succesfully"

cursor = db.cursor()
#cursor.execute('''
#   CREATE TABLE geoadd(city TEXT,
#                       pincode INTE, country TEXT)
#''')

cursor.execute('''INSERT INTO geoadd(city,pincode,country) VALUES(?,?,?)''',(city,pincode,country))
db.commit()
cursor.execute('''select * from geoadd''')
for row in cursor:
    print (row)
db.close()
#print txt.read()
#print jdata.read()


