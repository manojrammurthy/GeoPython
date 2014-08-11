from sys import argv
import urllib
import json

#script, filename = argv
pincode = raw_input("enter pincode> ")
country = raw_input("countryname > ")

url = "https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:"
url1 = url + pincode + "|country" + country
jdata = urllib.urlopen(url1)

# the output we get is json but we cannot query on this data 
# so we have to load this data as json in a variable
fp = json.load(jdata)
result = fp['results'][0]['geometry']['location']
#for rs in result:
    #print rs['lat']
print result['lat'] 
status = fp['status']
if status  == 'ZERO_RESULTS':
    print "indicates that the reverse geocoding was successful but returned no results"
elif status == 'INVALID_REQUEST':
    print "country and postal code may be wrong "
elif status == 'UNKNOWN_ERROR':
    print "UNKNOWN_ERROR may be due to server error"
#with open(filename, 'a') as outfile:
 #   json.dump(fp, outfile, ensure_ascii = False)

