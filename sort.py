lista = [3, 2, 1, 4]
pituus = len(lista)

print(lista)
x = 0

for x in range(pituus - 1):
    a = lista[x]
    b = lista[x + 1]
    c = 0
    if (a > b):
        print(a,b)
        c = b
        b = a
        a = c
        lista[x] = a
        lista[x + 1] = b

for x in range(pituus - 1):
    a = lista[x]
    b = lista[x + 1]
    c = 0
    if (a > b):
        print(a,b)
        c = b
        b = a
        a = c
        lista[x] = a
        lista[x + 1] = b

print(lista)

import json


"""luetaan tiedosto ja parsitaan se dictionary muotoon
tiedosto = open("D:\ohtek\Tapahtumat\ekat.json", "r")
luettu = (tiedosto.read())
kaupungit = json.loads(luettu)

print(kaupungit["data"][1]["event_dates"]["starting_day"])
kaupungit.sort()
print(kaupungit["data"][1]["event_dates"]["starting_day"])"""
         