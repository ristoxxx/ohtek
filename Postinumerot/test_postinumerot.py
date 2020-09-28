from postinumerot import hae_postinumerot
from postinumerot import lue_tiedosto
from postinumerot import hae_kaupunki

"""
vaihtoehto testidatan noutamiseen. Ei zero depency
json_url ="testdata.json"
data = lue_tiedosto(json_url)
"""

"""testidata"""
data = {
    "31401": "SOMERO",
    "31400": "SOMERO",
    "32210": "LOIMAA",
    "32200": "LOIMAA",
    "32201": "LOIMAA"
}

"""testaa pienellä kirjoitetun nimen"""
def test_hae_postinumerot_somero():    
    kaupunki = 'somero'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa SUURELLA kirjoitetun nimen"""
def test_hae_postinumerot_SOMERO():
    kaupunki = 'SOMERO'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa jos Ensimmäinen kirjain isolla"""
def test_hae_postinumerot_Somero():
    kaupunki = 'Somero'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa palauttaako tyhjä syöte tyhjän listan"""
def test_hae_postinumerot_if_empty():
    kaupunki = ''
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa mitä tapahtuu jos syöte ei löydy listalta"""
def test_hae_postinumerot_if_not_on_list():
    kaupunki = 'lvnslrvjr'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa mitä tapahtuu jos syötetään numero kun pyydetään nimeä"""
def test_hae_postinumerot_if_number():
    kaupunki = '00100'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa kaupungin hakeminen loimaan postinumerolla"""
def test_hae_kaupunki_loimaa():
    numero = '32200'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == 'LOIMAA'

"""testaa kaupungin hakeminen jos tyhjä syöte"""
def test_hae_kaupunki_if_empty():
    numero = ''
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''
    
"""testaa kaupungin hakeminen jos numeroa ei löydy"""    
def test_hae_kaupunki_if_not_found():
    numero = '69696'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''

"""testaa kaupungin hakeminen jos syötetään nimi kun pitäisi syöttää numero"""    
def test_hae_kaupunki_if_text():
    numero = 'LOIMAA'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''