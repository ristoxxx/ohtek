kaupungit = {
    'helsinki': 10100,
    'espoo': 10200,
    'vantaa': 10300,
    'vantaa': 10400
}

print("Kirjoita postinumero: ")
x = int(input())

for kaupunki, vakiluku in kaupungit.items():
    if vakiluku == x:
        print(kaupunki.upper())
