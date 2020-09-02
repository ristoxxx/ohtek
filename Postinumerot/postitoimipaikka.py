import json

"""luetaan tiedosto ja parsitaan se dictionary muotoon"""
tiedosto = open("D:\ohtek\postinumerot\postinumerot.json", "r")
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
        

        


