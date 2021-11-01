from Domain.inventar import getLocatie, getDescriere, getId
from Logic.CRUD import adaugaInventar, getById
from Logic.functionalitati import modificareLocatieInventare, concat_string_descriere, PretMaxim, \
    ordonareDupaPretAchizitie, sumaPreturiPerLocatie


def testModificareLocatieInventare():
    lista = []
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    locatieNoua = "9000"

    lista = modificareLocatieInventare(locatieNoua, lista)

    assert getLocatie(getById("2", lista)) == "9000"
    assert getLocatie(getById("4", lista)) == "9000"

def testConcatSTringDescriere():
    lista=[]
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adaugaInventar("5", "tableta", "munca", 4500.0, "1567", lista)
    string = "ok"
    pret = 3000.0

    lista = concat_string_descriere(lista, pret, string)

    assert getDescriere(getById("2", lista)) == "socializareok"
    assert getDescriere(getById("4", lista)) == "vizionare"


def testPretMax():
    lista = []
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adaugaInventar("5", "tableta", "munca", 4500.0, "7230", lista)
    preturi = PretMaxim(lista)
    assert len(preturi) == 2
    assert preturi["7230"] == 5000.0

def testOrdonareDupaPretAchzitie():
    lista = []
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adaugaInventar("5", "tableta", "munca", 4500.0, "7230", lista)

    rezultat = ordonareDupaPretAchizitie(lista)
    assert getId(rezultat[0]) == "4"
    assert getId(rezultat[1]) == "5"
    assert getId(rezultat[2]) == "2"

def testSumaPreturiPerLocatie():
    lista = []
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adaugaInventar("5", "tableta", "munca", 4500.0, "7230", lista)

    rezultat = sumaPreturiPerLocatie(lista)

    assert len(rezultat) == 2
    assert rezultat["7230"] == 9500.0



