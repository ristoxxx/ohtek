import json
import datetime
from datetime import date


"""luetaan tiedosto ja parsitaan se dictionary muotoon"""
tiedosto = open("D:\ohtek\Tapahtumat\ekat.json", "r")
luettu = (tiedosto.read())
kaupungit = json.loads(luettu)

print(kaupungit["data"][1]["event_dates"]["starting_day"])

apu = (kaupungit["data"][1]["event_dates"]["starting_day"])
date1 = apu[0:10]
date2 = "2020-11-18"

def get_date(a): 
    return date.fromisoformat((kaupungit["data"][a]["event_dates"]["starting_day"])[0:10])

print(get_date(5))


foo = {}

foo[0] = (0, get_date(0))
foo[1] = (1, get_date(1))
foo[2] = (2, get_date(2))
foo[3] = (3, get_date(3))


print(foo)

x = foo[0]
foo[0] = foo[1]
foo[1] = x

print(foo[0][0])    
def compare_date(a,b):
    date1 = date.fromisoformat(a)
    date2 = date.fromisoformat(b)
    return date1 < date2
print (compare_date(date1,date2))
