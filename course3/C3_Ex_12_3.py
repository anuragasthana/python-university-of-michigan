import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


start = 1
while start <= int(count):
    tags = soup('a')
    tag = tags[int(position)-1].get('href', None)
    print(tag)
    html = urllib.request.urlopen(tag).read()
    soup = BeautifulSoup(html, 'html.parser')
    start = start + 1
