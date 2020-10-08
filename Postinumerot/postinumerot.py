import json

json_url="postinumerot.json"

def lue_tiedosto(osoite):
    
    """luetaan tiedosto ja parsitaan se dictionary muotoon"""
    tiedosto = open(osoite, "r")
    luettu = (tiedosto.read())
    lista = json.loads(luettu)
    return lista

def kysy_toiminto():
    """kysytaan kayttajalta halutaanko etsia 
    kaupungin vai postinumeron perusteella"""
    print("Etsitaanko postinumeroa (P) vai kaupunkia (K): ", end = "")
    syote = input()
    return syote


def kysy_kaupunki():
    """pyydeaan kayttajaa syottamaan postinumero ja luetaan syote"""
    print("Kirjoita postitoimipaikka: ", end="")
    syote = input()
    return syote

def kysy_postinumero():
    """pyydetaan kayttajaa syottamaan postinumero ja luetaan syote"""
    print("Kirjoita postinumero: ", end="")
    syote = input()
    return syote

def hae_kaupunki(kaupungit, numero):
    for postinumero, kaupunki in kaupungit.items():
        if postinumero == numero:
            print(kaupunki.upper())
            return kaupunki.upper()
    return ''

def hae_postinumerot(kaupungit, nimi):
    """kaydaan lista lapi ja jos postitoimipaikka loytyy niin lisataan 
    listalle kaikki postinumerot samalla muotoillen lista tulostukseen"""
    nimi = nimi.upper()
    lista = []
    for postinumero, kaupunki in kaupungit.items():
        if kaupunki == nimi:
            lista.append(postinumero.upper() + ", ")
    if lista == []:
        lista.append(", ")
    
    lista[-1] = lista[-1].strip(", ")
    

    """def tulosta(lista):"""
    """tulostetaan listalla olevat postinumerot"""
    print("Postinumerot: ", end="")
    for numero in range(len(lista)): 
        print(lista[numero], end="") 
    return lista
"""print(kaupungit)"""

def main():
    print("\033[1;32;40m")
    kaupungit = lue_tiedosto(json_url)
    valinta = 'X' 
    while valinta != 'K' and valinta != 'P':
        valinta = kysy_toiminto()
        if valinta == 'K':
            nimi = kysy_kaupunki()   
            hae_postinumerot(kaupungit, nimi)
        if valinta == 'P':
            numero = kysy_postinumero()
            hae_kaupunki(kaupungit, numero)
    
if __name__ == "__main__":
    main()
