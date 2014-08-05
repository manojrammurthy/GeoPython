import urllib
params = urllib.urlencode({'postal_code': raw_input("> "), 'country':raw_input("> ")})
print params
f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?components=", params)
print f.read()