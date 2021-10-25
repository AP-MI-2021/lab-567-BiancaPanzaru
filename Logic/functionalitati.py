from Domain.inventar import creeazaInventar, getId, getNume, getDescriere, getPret


def modificareLocatieInventare(locatieNoua, lista):
    listaNoua = []
    for inventar in lista:
        inventarNou = creeazaInventar(getId(inventar), getNume(inventar), getDescriere(inventar), getPret(inventar), locatieNoua)
        listaNoua.append(inventarNou)
    return listaNoua