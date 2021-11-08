from Domain.inventar import toString, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaInventar, stergeInventar, modificaInventar, getById
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
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare tot inventarul.")
    print("x. Iesire")

def uiAdaugareInventar(lista, undoList, redoList, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            descriere = input("Dati descrierea: ")
            pret = float(input("Dati pretul: "))
            locatie = input("Dati locatia: ")
        else:
            id = obiecte[0]
            nume = obiecte[1]
            descriere = obiecte[2]
            pret = obiecte[3]
            locatie = obiecte[4]
        rezultat = adaugaInventar(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergereInventar(lista, undoList, redoList, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul obiectul din inventar ce trebuie sters: ")
        else:
            id = obiecte[0]
        rezultat = stergeInventar(id, lista)
        #inventarDeSters = getById(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareInventar(lista, undoList, redoList, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul obiectului din inventar de modificat: ")
            nume = input("Dati noul nume: ")
            descriere = input("Dati noua descriere: ")
            pret = float(input("Dati noul pret: "))
            locatie = input("Dati noua locatie: ")
        else:
            id = obiecte[0]
            nume = obiecte[1]
            descriere = obiecte[2]
            pret = obiecte[3]
            locatie = obiecte[4]
        rezultat = modificaInventar(id, nume, descriere, pret, locatie, lista)
        inventarVechi = getById(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for inventar in lista:
        print(toString(inventar))


def uiModificareLocatieInventare(lista, undoList, redoList, obiecte):
    try:
        if len(obiecte) == 0:
            locatieNoua = input("Dati noua locatie a inventarelor: ")
        else:
            locatieNoua = obiecte[0]
        rezultat = modificareLocatieInventare(locatieNoua, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiConcatStringDescriere(lista, undoList, redoList, obiecte):
    try:
        if len(obiecte) == 0:
            pret = float(input("Dati pretul: "))
            string = input("Dati textul ce trebuie concatenat descrierii obiectului: ")
        else:
            pret = obiecte[0]
            string = obiecte[1]
        rezultat = concat_string_descriere(lista, pret, string)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretMax(lista):
    preturi = PretMaxim(lista)
    for locatie in preturi:
        print("Locatia {} are pretul maxim {}".format(locatie, preturi[locatie]))


def uiOrdonareDupaPretAchzitie(lista, undoList, redoList):
    rezultat = ordonareDupaPretAchizitie(lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiSumaPreturiPerLocatie(lista):
    rezultat = sumaPreturiPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def undo(lista, undoList, redoList):
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    else:
        print("Nu se poate face undo!")
    return lista


def redo(lista, undoList, redoList):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    else:
        print("Nu se poate face redo!")
    return lista


def runMenu(lista):
    undoList = []
    redoList = []
    obiecte = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
        elif optiune == "2":
            lista = uiStergereInventar(lista, undoList, redoList, obiecte)
        elif optiune == "3":
            lista = uiModificareInventar(lista, undoList, redoList, obiecte)
        elif optiune == '4':
            lista = uiModificareLocatieInventare(lista, undoList, redoList, obiecte)
        elif optiune == "5":
            lista = uiConcatStringDescriere(lista, undoList, redoList, obiecte)
        elif optiune == "6":
            lista = uiPretMax(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaPretAchzitie(lista, undoList, redoList)
        elif optiune == "8":
            lista = uiSumaPreturiPerLocatie(lista)
        elif optiune == "u":
            lista = undo(lista, undoList, redoList)
        elif optiune == "r":
            lista = redo(lista, undoList, redoList)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")