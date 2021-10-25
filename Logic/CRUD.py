from Domain.inventar import creeazaInventar, getId


def adaugaInventar(id, nume, descriere, pret, locatie, lista):
    '''

    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :param lista:
    :return: o lista continand lista veche + noul obiect
    '''

    inventar = creeazaInventar(id, nume, descriere, pret, locatie)
    return lista + [inventar]

def getById(id, lista):
    '''
    ia obiectul din inventar cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de obiecte din inventar
    :return: obiectul cu id-ul dat sau None, daca nu exista obiectul cu id-ul dat
    '''
    for inventar in lista:
        if getId(inventar) == id:
            return inventar
    return None

def stergeInventar(id, lista):
    '''
    sterge un obiect dintr-o lista dupa id
    :param id: id-ul obiectului ce trebuie sters
    :param lista:lista de obiecte din inventar
    :return: lista dupa ce a fost facuta modificarea
    '''
    return [inventar for inventar in lista if getId(inventar) != id]

def modificaInventar(id, nume, descriere, pret, locatie, lista):
    listaNoua = []
    for inventar in lista:
        if getId(inventar) == id:
            inventarNou = creeazaInventar(id, nume, descriere, pret, locatie, lista)
            listaNoua.append(inventarNou)
        else:
            listaNoua.append(inventar)
    return listaNoua

