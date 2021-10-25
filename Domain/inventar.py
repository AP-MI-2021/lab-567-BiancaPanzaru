def creeazaInventar(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce retine un inventar
    :param id: id-ul inventarului - string
    :param nume: numele inventarului - string
    :param descriere: descrierea inventarului - string
    :param pret: pretul obiectului - float
    :param locatie: locatia obiectului - string
    :return:un dictionar ce retine un obiect din inventar
    """
    return [id, nume, descriere, pret, locatie]
    """
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }
    """


def getId(inventar):
    """
    da id-ul unui obiect
    :param inventar: o lista de tip inventar
    :return: id-ul obiectului - string
    """
    return inventar[0]
    #return inventar["id"]

def getNume(inventar):
    """
    da numele unui obiect
    :param inventar: o lista de tip inventar
    :return: numele obiectului - string
    """
    return inventar[1]
    #return inventar["nume"]

def getDescriere(inventar):
    """
    da descrierea unui obiect
    :param inventar: o lista de tip inventar
    :return: descrierea obiectului - string
    """
    return inventar[2]
    #return inventar["descriere"]

def getPret(inventar):
    """
    da pretul unui obiect
    :param inventar: o lista de tip inventar
    :return: pretul obiectului - float
    """
    return inventar[3]
    #return inventar["pret"]

def getLocatie(inventar):
    """
    da locatia unui obiect
    :param inventar: o lista de tip inventar
    :return: locatia obiectului - string
    """
    return inventar[4]
    #return inventar["locatie"]

def toString(inventar):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        getId(inventar),
        getNume(inventar),
        getDescriere(inventar),
        getPret(inventar),
        getLocatie(inventar)
    )
