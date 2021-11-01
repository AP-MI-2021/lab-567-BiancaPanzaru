from Domain.inventar import creeazaInventar, getId, getNume, getDescriere, getPret, getLocatie


def modificareLocatieInventare(locatieNoua, lista):
    """
    Modifica locatia inventarelor la o locatie data.
    :param locatieNoua: string
    :param lista: lista de inventare
    :return: lista modificata
    """
    if len(locatieNoua) != 4:
        raise ValueError("Locatia noua trebuie sa fie formata din 4 caractere")
    listaNoua = []
    for inventar in lista:
        inventarNou = creeazaInventar(getId(inventar), getNume(inventar), getDescriere(inventar), getPret(inventar), locatieNoua)
        listaNoua.append(inventarNou)
    return listaNoua

def concat_string_descriere(lista, pret, string):
    """
    Concateneaza un string la descrierea obiectelor cu un pret mai mare decat un pret dat.
    :param lista: lista de inventare
    :param pret: pretul citit
    :param string: textul ce trebuie concatenat
    :return: lista modificata
    """
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv")
    listaNoua=[]
    for inventar in lista:
        if getPret(inventar) > pret:
            s = getDescriere(inventar) + string
            inventarNou = creeazaInventar(getId(inventar), getNume(inventar), s, getPret(inventar), getLocatie(inventar))
            listaNoua.append(inventarNou)
        else:
            listaNoua.append(inventar)
    return listaNoua

def PretMaxim(lista):
    """
    Determina cel mai mare pret per locatie.
    :param lista: lista de inventare
    :return: pretul cel mai mare pentru fiecare locatie
    """
    preturi = {}
    for inventar in lista:
        locatie = getLocatie(inventar)
        if locatie in preturi:
            if getPret(inventar) > preturi[locatie]:
                preturi[locatie] = getPret(inventar)
        else:
            preturi[locatie] = getPret(inventar)
    return preturi

def ordonareDupaPretAchizitie(lista):
    """
    Ordoneaza obiectele crescator dupa pretul de achizitie
    :param lista: lista de inventare
    :return: lista ordonata
    """
    return sorted(lista, key= lambda inventar: getPret(inventar))


def sumaPreturiPerLocatie(lista):
    """
    Calculeaza suma preturilor pentru fiecare locatie
    :param lista: lista de inventare
    :return: suma preturilor per locatie
    """
    rezultat = {}
    for inventar in lista:
        locatie = getLocatie(inventar)
        pret = getPret(inventar)
        if locatie in rezultat:
            rezultat[locatie] = rezultat[locatie] + pret
        else:
            rezultat[locatie] = pret
    return rezultat