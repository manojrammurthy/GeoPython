import urllib
import json
import sqlite3
import requests
from bs4 import BeautifulSoup
session = requests.session()

def fetchCode(country):
    page = session.get('http://en.wikipedia.org/wiki/ISO_3166-1')
    soup = BeautifulSoup(page.text).find('table', {'class': 'wikitable'})
    tablerows = soup.findAll('tr')
    for tr in tablerows:
        td = tr.findAll('td')
        if td:
            if td[0].text.lower() == country.lower():
                numeric_code = td[3].text
                ISO_code = td[4].text
                return numeric_code,ISO_code

#var,var1=fetchCode(raw_input('Enter Country Name:'))
#print var,var1
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
ISO_code , numeric_code = fetchCode(country)
print lat, lng 
print city
print "numeric_code is %s and ISO_code is %s" %(ISO_code,numeric_code)

db = sqlite3.connect('/home/lenovo/workspace/GeoPython/db/mydb')
print "opened databaase succesfully"

cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS geoadd(city TEXT,
                       pincode INTE, country TEXT)
''')
#cursor.execute('''ALTER TABLE geoadd add column numericcode INTEGER''')
#cursor.execute('''ALTER TABLE geoadd add column ISOcode TEXT''')
cursor.execute('''INSERT INTO geoadd(city,pincode,country,lat,lng,numericcode,ISOcode) VALUES(?,?,?,?,?,?,?)''',(city,pincode,country,lat,lng,numeric_code,ISO_code))
db.commit()
cursor.execute('''select * from geoadd''')

for row in cursor:
    print (row)
db.close()
#print txt.read()
#print jdata.read()


