from Domain.inventar import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaInventar, stergeInventar, getById


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
    lista = adaugaInventar("1", "telefon", "vorbire", 1500, "Cluj", [])
    lista = adaugaInventar("2", "tableta", "vorbire", 1500, "Cluj", [])

    lista = stergeInventar("1", lista)
    assert getById("1") is None
    assert getById("2") is not None