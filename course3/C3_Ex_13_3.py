import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    uh = urllib.request.urlopen(url)
    data = uh.read()
    info = data.decode()

    try:
        js = json.loads(info)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("=====Failure to retrieve=====")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    print(js['results'][0]['place_id'])