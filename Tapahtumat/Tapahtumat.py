import json
import datetime
from datetime import date


"""luetaan tiedosto ja parsitaan se dictionary muotoon"""
tiedosto = open("D:\ohtek\Tapahtumat\ekat.json", "r")
luettu = (tiedosto.read())
kaupungit = json.loads(luettu)

"""pituus = (len(kaupungit["data"]))"""
pituus = 100

def get_date(a): 
    return date.fromisoformat((kaupungit["data"][a]["event_dates"]["starting_day"])[0:10])

def compare_date(a,b):
    return a < b

foo = {}
for x in range(pituus):
    foo[x] = (x, get_date(x))

def sorttaa():
    for j in range(pituus -1):
        for x in range(pituus -1):
            a = foo[x][1]
            b = foo[x + 1][1]
            if(compare_date(a,b)):
                y = x + 1
                d = foo[x]
                foo[x] = foo[y]
                foo[y] = d
    return foo

foo = sorttaa()
ed_paiva = ""
bar = {}
"""def sijoita():"""
for s in range(pituus -1):
    bar[s] = (kaupungit["data"][(foo[s][0])])
    paiva = ((bar[s]["event_dates"]["starting_day"])[0:10])
    if(paiva != ed_paiva):
        print(paiva)
    ed_paiva = paiva
    print("  ", ((bar[s]["event_dates"]["starting_day"])[11:19]), bar[s]["name"]["fi"])
        
"""bar = sijoita()"""