# In this assignment you will write a Python program. The program will prompt for a URL, read the JSON data from 
# that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

curl = 'http://py4e-data.dr-chuck.net/comments_1425739.json'

url =input("Enter location:  ")
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data=uh.read()
print('Retrieved', len(data), 'characters')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
total = 0
try:
    js = json.loads(data)
except:
    js = None
    
info = json.loads(data)

for item in info['comments']:
    count += 1
    total += int(item["count"])
    
    
    print('Count : ', count )
    print('Sum : ', total)


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        # print(data)
        continue

    # print(json.dumps(js, indent=4))

    placeID = js['results'][0]['place_id']
 
    
    print(placeID)    