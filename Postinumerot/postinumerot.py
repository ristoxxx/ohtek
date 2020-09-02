import json

"""luetaan tiedosto ja parsitaan se dictionary muotoon"""
tiedosto = open("D:\ohtek\postinumerot\postinumerot.json", "r")
luettu = (tiedosto.read())
kaupungit = json.loads(luettu)

"""pyydetään käyttäjää syöttämään postinumero ja luetaan syöte"""
print("Kirjoita postitoimipaikka: ", end="")
x = input()
x = x.upper()
print("Postinumerot: ", end="")

"""käydään lista läpi ja jos postitoimipaikka löytyy niin lisätään 
listalle kaikki postinumerot samalla muotoillen lista tulostukseen"""
lista = []
for postinumero, kaupunki in kaupungit.items():
    if kaupunki == x:
        lista.append(postinumero.upper() + ", ")

lista[-1] = lista[-1].strip(", ")

"""tulostetaan listalla olevat postinumerot"""
for numero in range(len(lista)): 
    print(lista[numero], end="") 

        

        


