import json
import datetime
from datetime import date
import urllib.request

"""osoite josta tiedot haetaan(?limit=numero jos haluaa testata pienmmällä rivimmäärällä)"""
json_url ="http://open-api.myhelsinki.fi/v1/events/"

"""luetaan tiedot ylläolevasta osoitteesta"""
def hae_tiedot():
    # https://docs.python.org/3/howto/urllib2.html
    with urllib.request.urlopen(json_url) as response:
        # https://docs.python.org/3/library/json.html
        return json.loads(response.read())


"""haetaan päivämäärä alkuperäisestä tiedostosta"""
def hae_paiva(a):
    try:
        paivays = date.fromisoformat((tiedot["data"][a]["event_dates"]["starting_day"])[0:10])
        return paivays
    except TypeError:
        return date.fromisoformat("2000-01-01")

"""haetaan päivämäärä uudelleenjärjestetystä tietorakenteesta"""
def hae_uusi_paiva(a):
    try:
        paivays = ((uusi_hakemisto[a]["event_dates"]["starting_day"])[0:10])
        return paivays
    except TypeError:
        return date.fromisoformat("2000-01-01")
   
"""haetaan kellonaika uudelleenjärjestetystä tietorakenteesta"""    
def hae_kellonaika(a):
    try:
        aika = ((uusi_hakemisto[a]["event_dates"]["starting_day"])[11:19])
        return aika
    except TypeError:
        return ("00:00:00")

"""verrataan kahta päivämäärätietoa keskenään"""
def vertaa_paivays(a,b):
    return a < b

def jarjesta():
    for j in range(pituus -1):
        for x in range(pituus -1):
            a = hakemisto[x][1]
            b = hakemisto[x + 1][1]
            if(vertaa_paivays(a,b)):
                y = x + 1
                d = hakemisto[x]
                hakemisto[x] = hakemisto[y]
                hakemisto[y] = d
    return hakemisto


tiedot = hae_tiedot()
"""pituus = tietueiden lukumäärä"""
pituus = (len(tiedot["data"]))

"""muodostetaan erillinen hakemisto päivämääristä ja tietueen sijainnista"""
hakemisto = {}
for x in range(pituus):
    hakemisto[x] = (x, hae_paiva(x))

"""järjestetään hakemisto päiväyksen mukaan. huom. ei huomioi kellonaikoja"""
hakemisto = jarjesta()

"""kootaan uusi tietorakenne järjestämällä talkuperäiset tietueet
muodostetun hakemiston avulla. samalla myös tulostetaan uuden listan rivit.
ei ehkä elegantein ratkaisu"""

ed_paiva = ""
uusi_hakemisto = {}

for s in range(pituus -1):
    uusi_hakemisto[s] = (tiedot["data"][(hakemisto[s][0])])
    paiva = hae_uusi_paiva(s)
    if(paiva != ed_paiva):
        print(paiva)
    ed_paiva = paiva
    print("  ", hae_kellonaika(s), uusi_hakemisto[s]["name"]["fi"])