from Domain.inventar import creeazaInventar, getId, getNume, getDescriere, getPret


def modificareLocatieInventare(locatieNoua, lista):
    """
    Modifica locatia inventarelor la o locatie data.
    :param locatieNoua: string
    :param lista: lista de inventare
    :return: lista modificata
    """
    listaNoua = []
    for inventar in lista:
        inventarNou = creeazaInventar(getId(inventar), getNume(inventar), getDescriere(inventar), getPret(inventar), locatieNoua)
        listaNoua.append(inventarNou)
    return listaNoua