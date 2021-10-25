#from Domain.inventar import creeazaInventar, getId, getNume, getDescriere, getPret, getLocatie
from Domain.inventar import creeazaInventar, getId, getNume, getDescriere, getPret, getLocatie


def testInventar():
    inventar = creeazaInventar("1", "telefon", "vorbire", 1500, "Cluj")

    assert getId(inventar) == "1"
    assert getNume(inventar) == "telefon"
    assert getDescriere(inventar) == "vorbire"
    assert getPret(inventar) == 1500
    assert getLocatie(inventar) == "Cluj"