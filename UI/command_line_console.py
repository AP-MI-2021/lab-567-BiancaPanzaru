from Domain.inventar import toString
from Logic.CRUD import adaugaInventar, stergeInventar


def showAll(lista):
    for inventar in lista:
        print(toString(inventar))

def main_line(lista):
    while True:
        givenString = input()
        if givenString == "ajutor":
            print("add, id, nume, descriere, pret, locatie")
            print("delete,id")
            print("showall")
            print("exit")
        else:
            optiuni = givenString.split(";")
            if optiuni[0] == "exit":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if(opt[0] == "add"):
                        try:
                            lista = adaugaInventar(opt[1], opt[2], opt[3], float(opt[4]), opt[5], lista)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showall":
                        showAll(lista)
                    elif opt[0] == "delete":
                        lista = stergeInventar(opt[1], lista)
                    else:
                        print("Optiune gresita! Scrieti 'ajutor' pentru a vedea optiunile disponibile")

