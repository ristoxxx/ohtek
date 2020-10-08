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

"""testaa pienella kirjoitetun nimen"""
def test_hae_postinumerot_somero():    
    kaupunki = 'somero'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa SUURELLA kirjoitetun nimen"""
def test_hae_postinumerot_SOMERO():
    kaupunki = 'SOMERO'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa jos Ensimmainen kirjain isolla"""
def test_hae_postinumerot_Somero():
    kaupunki = 'Somero'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['31401, ', '31400']

"""testaa palauttaako tyhja syote tyhjan listan"""
def test_hae_postinumerot_if_empty():
    kaupunki = ''
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa mita tapahtuu jos syote ei loydy listalta"""
def test_hae_postinumerot_if_not_on_list():
    kaupunki = 'lvnslrvjr'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa mita tapahtuu jos syotetaan numero kun pyydetaan nimea"""
def test_hae_postinumerot_if_number():
    kaupunki = '00100'
    lista = hae_postinumerot(data, kaupunki)
    assert lista == ['']

"""testaa kaupungin hakeminen loimaan postinumerolla"""
def test_hae_kaupunki_loimaa():
    numero = '32200'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == 'LOIMAA'

"""testaa kaupungin hakeminen jos tyhja syote"""
def test_hae_kaupunki_if_empty():
    numero = ''
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''
    
"""testaa kaupungin hakeminen jos numeroa ei loydy"""    
def test_hae_kaupunki_if_not_found():
    numero = '69696'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''

"""testaa kaupungin hakeminen jos syotetaan nimi kun pitaisi syottaa numero"""    
def test_hae_kaupunki_if_text():
    numero = 'LOIMAA'
    kaupunki = hae_kaupunki(data, numero)
    assert kaupunki == ''
