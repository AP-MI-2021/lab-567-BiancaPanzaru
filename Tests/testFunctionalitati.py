from Domain.inventar import getLocatie
from Logic.CRUD import adaugaInventar, getById
from Logic.functionalitati import modificareLocatieInventare


def testModificareLocatieInventare():
    lista = []
    lista = adaugaInventar("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adaugaInventar("2", "telefon", "socializare", 5000.0, "7230", lista)
    locatieNoua = "9000"

    lista = modificareLocatieInventare(locatieNoua, lista)

    assert getLocatie(getById("2", lista)) == "9000"
    assert getLocatie(getById("4", lista)) == "9000"