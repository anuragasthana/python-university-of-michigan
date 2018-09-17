import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter url: ')
    if len(url) < 1: break


    uh = urllib.request.urlopen(url)
    data = uh.read()
    info = data.decode()
    datab = json.loads(info)
    comments = datab['comments']
    sum = 0

    for comment in comments:
        sum = sum + int(comment['count'])

    print(sum)