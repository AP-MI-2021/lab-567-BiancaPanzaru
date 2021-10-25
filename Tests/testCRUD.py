from Domain.inventar import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaInventar, stergeInventar, getById, modificaInventar


def testAdaugaInventar():
    lista = adaugaInventar("1", "telefon", "vorbire", 1500, "Cluj", [])

    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "telefon"
    assert getDescriere(lista[0]) == "vorbire"
    assert getPret(lista[0]) == 1500
    assert getLocatie(lista[0]) == "Cluj"


def testStergeInventar():
    lista = []
    lista = adaugaInventar("1", "telefon", "vorbire", 1500, "Cluj", lista)
    lista = adaugaInventar("2", "tableta", "vorbire", 1500, "Cluj", lista)

    lista = stergeInventar("1", lista)
    assert getById("1") is None
    assert getById("2") is not None

def testGetById():
    lista = []
    lista = adaugaInventar("1", "telefon", "vorbire", 1500, "2348", lista)
    lista = adaugaInventar("2", "tableta", "vorbire", 1500, "Cluj", lista)
    assert getById("2", lista) is not None
    assert getById("5", lista) is None

def testModificaInventar():
    lista = []
    lista = adaugaInventar("1", "telefon", "vorbire", 1500, "2348", lista)
    lista = adaugaInventar("2", "telefon", "vorbire", 1500, "7564", lista)
    lista = modificaInventar("1", "iphone", "vorbire", 1500, "cluj", lista)
    inventarModificat = getById("1", lista)
    assert getNume(inventarModificat) == "iphone"

