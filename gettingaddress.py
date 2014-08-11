import urllib
import json
import sqlite3

print "Enter the pincode of area that you want to see"
pincode = raw_input("> ")
print "Enter  the country name "
country = raw_input("> ")
url = "https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:"
url1 = url + pincode + "|country:" + country
print  url1
#while True:
jdata = urllib.urlopen(url1)
fp = json.load(jdata)
  #  if
print fp['status']
#print fp["results"]
result = fp['results'][0]['geometry']['location']
lat , lng = result['lat'], result['lng']
city = json.dumps([s['address_components'][2]['long_name'] for s in fp['results']], indent=2)
print lat, lng 
print city
db = sqlite3.connect('/home/lenovo/workspace/GeoPython/db/mydb')
print "opened databaase succesfully"

cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS geoadd(city TEXT,
                       pincode INTE, country TEXT)
''')
#cursor.execute('''ALTER TABLE geoadd add column lat float''')
#cursor.execute('''ALTER TABLE geoadd add column lng float''')
cursor.execute('''INSERT INTO geoadd(city,pincode,country,lat,lng) VALUES(?,?,?,?,?)''',(city,pincode,country,lat,lng))
db.commit()
cursor.execute('''select * from geoadd''')

for row in cursor:
    print (row)
db.close()
#print txt.read()
#print jdata.read()


