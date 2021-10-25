from Domain.inventar import toString
from Logic.CRUD import adaugaInventar, stergeInventar, modificaInventar
from Logic.functionalitati import modificareLocatieInventare


def printMenu():
    print("1. Adaugare inventar.")
    print("2. Stergere inventar.")
    print("3. Modificare inventar.")
    print("4. Modificare locatie inventare.")
    print("a. Afisare tot inventarul.")
    print("x. Iesire")

def uiAdaugareInventar(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul: "))
    locatie = input("Dati locatia: ")
    return adaugaInventar(id, nume, descriere, pret, locatie, lista)

def uiStergereInventar(lista):
    id = input("Dati id-ul obiectul din inventar ce trebuie sters: ")
    return stergeInventar(id, lista)

def uiModificareInventar(lista):
    id = input("Dati id-ul obiectului din inventar de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret: "))
    locatie = input("Dati noua locatie: ")
    return modificaInventar(id, nume, descriere, pret, locatie, lista)


def showAll(lista):
    for inventar in lista:
        print(toString(inventar))


def uiModificareLocatieInventare(lista):
    locatieNoua = input("Dati noua locatie a inventarelor: ")
    return modificareLocatieInventare(locatieNoua, lista)


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugareInventar(lista)
        elif optiune == "2":
            lista = uiStergereInventar(lista)
        elif optiune == "3":
            lista = uiModificareInventar(lista)
        elif optiune == '4':
            lista = uiModificareLocatieInventare(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")