from Domain.inventar import toString
from Logic.CRUD import adaugaInventar, stergeInventar, modificaInventar
from Logic.functionalitati import modificareLocatieInventare, concat_string_descriere, PretMaxim, \
    ordonareDupaPretAchizitie, sumaPreturiPerLocatie


def printMenu():
    print("1. Adaugare inventar.")
    print("2. Stergere inventar.")
    print("3. Modificare inventar.")
    print("4. Modificare locatie inventare.")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație.")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("a. Afisare tot inventarul.")
    print("x. Iesire")

def uiAdaugareInventar(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input("Dati pretul: "))
        locatie = input("Dati locatia: ")
        return adaugaInventar(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergereInventar(lista):
    try:
        id = input("Dati id-ul obiectul din inventar ce trebuie sters: ")
        return stergeInventar(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiModificareInventar(lista):
    try:
        id = input("Dati id-ul obiectului din inventar de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        return modificaInventar(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for inventar in lista:
        print(toString(inventar))


def uiModificareLocatieInventare(lista):
    try:
        locatieNoua = input("Dati noua locatie a inventarelor: ")
        return modificareLocatieInventare(locatieNoua, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiConcatStringDescriere(lista):
    try:
        pret = float(input("Dati pretul: "))
        string = input("Dati textul ce trebuie concatenat descrierii obiectului: ")
        return concat_string_descriere(lista, pret, string)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretMax(lista):
    preturi = PretMaxim(lista)
    for locatie in preturi:
        print("Locatia {} are pretul maxim {}".format(locatie, preturi[locatie]))

def uiOrdonareDupaPretAchzitie(lista):
    showAll(ordonareDupaPretAchizitie(lista))

def uiSumaPreturiPerLocatie(lista):
    rezultat = sumaPreturiPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


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
        elif optiune == "5":
            lista = uiConcatStringDescriere(lista)
        elif optiune == "6":
            lista = uiPretMax(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaPretAchzitie(lista)
        elif optiune == "8":
            lista = uiSumaPreturiPerLocatie(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")