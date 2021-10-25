def creeazaInventar(id, nume, descriere, pret, locatie):
    '''
    creeaza un dictionar ce retine un inventar
    :param id: id-ul inventarului - string
    :param nume: numele inventarului - string
    :param descriere: descrierea inventarului - string
    :param pret: pretul obiectului - float
    :param locatie: locatia obiectului - string
    :return:un dictionar ce retine un obiect din inventar
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }

def getId(inventar):
    '''
    da id-ul unui obiect
    :param inventar: un dictionar de tip inventar
    :return: id-ul obiectului - string
    '''
    return inventar["id"]

def getNume(inventar):
    return inventar["nume"]

def getDescriere(inventar):
    return inventar["descriere"]

def getPret(inventar):
    return inventar["pret"]

def getLocatie(inventar):
    return inventar["locatie"]

def toString(inventar):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        getId(inventar),
        getNume(inventar),
        getDescriere(inventar),
        getPret(inventar),
        getLocatie(inventar)
    )
