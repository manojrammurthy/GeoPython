import urllib
import json
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
print json.dumps([s['address_components'][2]['long_name'] for s in fp['results']], indent=2)
#print txt.read()
print jdata.read()


