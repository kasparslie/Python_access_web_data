import urllib.request as ur
import xml.etree.ElementTree as ET
import ssl

url = input('Enter location: ')
print('Retrieving', url)
data = ur.urlopen(url).read()
print('Retrieved', len(data), 'characters')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tree = ET.fromstring(data)
print(tree)
results = tree.findall('comments/comment')
print(results)
count = 0
sum = 0
for item in results:
    x = int(item.find('count').text)
    count = count +1
    sum = sum + x
    
    print('Count : ', count )
    print('Sum : ', sum)
    