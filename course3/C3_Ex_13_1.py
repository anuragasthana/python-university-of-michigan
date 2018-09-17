import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)

counts = tree.findall('.//count')
sum = 0

for count in counts:
    sum = int(count.text) + sum

print(sum)