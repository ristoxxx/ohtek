import json
import urllib.request

json_url ="D:\ohtek\postinumerot\postinumerot.json"

def hae_postinumerot():
    with urllib.request.urlopen(json_url) as response:
        print ("moi")
        return json.loads(response.read)

"""luetaan tiedosto ja parsitaan se dictionary muotoon"""
tiedosto = open(json_url, "r")
luettu = (tiedosto.read())
kaupungit = json.loads(luettu)

"""pyydetään käyttäjää syöttämään postinumero ja luetaan syöte"""
print("Kirjoita postinumero: ")
x = input()

"""käydään lista läpi ja jos postinumero löytyy niin tulostetaan
postitoimipaikan nimi"""
for postinumero, kaupunki in kaupungit.items():
    if postinumero == x:
        print(kaupunki.upper())
        

        


