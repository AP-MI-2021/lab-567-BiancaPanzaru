from Domain.inventar import getNume, getPret, getLocatie, getDescriere, getId
from Logic.CRUD import getById
from UI.console import uiAdaugareInventar, undo, redo, uiStergereInventar, uiModificareInventar, \
    uiModificareLocatieInventare, uiConcatStringDescriere, uiOrdonareDupaPretAchzitie


def test_Undo_Redo():
#1 lista goala
    lista = []
    undoList = []
    redoList = []

#2 adaugam un obiect
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)

#3 adaugam inca un obiect
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)

#4 adaugam inca un obiect
    obiecte = [3, "telefon", "socializare", 4500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)

    assert len(lista) == 3

#5 undo scoate ultimul obiect adaugat
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(2, lista) is not None
    assert getById(3, lista) is None

#6 inca un undo scoate penultimul obiect
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None

#7 inca un undo scoate si primul obiect adaugat
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(2, lista) is None

#8 inca un undo nu va face nimic
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(2, lista) is None

#9 adaugam trei obiecte
    obiecte = [1, "telefon", "socializare", 3500.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "ceas", "ora", 900.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [3, "calculator", "work", 9500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)

    assert len(lista) == 3

#10 redo nu face nimic
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(3, lista) is not None

#11 doua undo-uri scot ultimele 2 obiecte
    lista = undo(lista, undoList, redoList)
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None

#12 redo anuleaza ultimul undo, daca ultima operatie e undo
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None

#13 redo anuleaza si primul undo
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None

#14 doua undo-uri scot ultimele 2 obiecte
    lista = undo(lista, undoList, redoList)
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None

#15 adaugam un obiect
    obiecte = [4, "bijuterie", "aur", 500.0, "4444"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)

    assert len(lista) == 2

#16 redo nu face nimic deoarece ultima operatie nu este undo
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(4, lista) is not None

#17 undo anuleaza adaugarea obiectului cu id 4
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(4, lista) is None

#18 undo anuleaza adaugarea obiectului cu id 1
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(4, lista) is None

#19 se anuleaza ultimele 2 undo-uri
    lista = redo(lista, undoList, redoList)
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is None

#20 redo nu face nimic
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(4, lista) is not None
    assert getById(3, lista) is None

#21 test undo\redo stergere inventar
    lista = []
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [3, "telefon", "socializare", 4500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte= [1]
    lista = uiStergereInventar(lista, undoList, redoList, obiecte)
    assert len(lista) == 2
    assert getById(1, lista) is None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None
    lista = undo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None
    lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById(1, lista) is None
    assert getById(2, lista) is not None

#22 test undo\redo modificare inventar
    lista = []
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [3, "telefon", "socializare", 4500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [1, "calculator", "jocuri", 9800.0, "4444"]
    lista = uiModificareInventar(lista, undoList, redoList, obiecte)
    assert len(lista) == 3
    assert getNume(getById(1, lista)) == "calculator"
    assert getPret(getById(1, lista)) == 9800.0
    lista = undo(lista, undoList, redoList)
    assert getNume(getById(1, lista)) == "tv"
    assert getPret(getById(1, lista)) == 5000.0
    lista = redo(lista, undoList, redoList)
    assert getNume(getById(1, lista)) == "calculator"
    assert getPret(getById(1, lista)) == 9800.0

#23 test undo\redo modifcare locatie
    lista = []
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [3, "telefon", "socializare", 4500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = ["5555"]
    lista = uiModificareLocatieInventare(lista, undoList, redoList, obiecte)
    assert len(lista) == 3
    assert getLocatie(getById(1, lista)) == "5555"
    assert getLocatie(getById(2, lista)) == "5555"
    assert getNume(getById(1, lista)) == "tv"
    lista = undo(lista, undoList, redoList)
    assert getLocatie(getById(1, lista)) == "1111"
    assert getLocatie(getById(2, lista)) == "2222"
    lista = redo(lista, undoList, redoList)
    assert getLocatie(getById(1, lista)) == "5555"
    assert getLocatie(getById(2, lista)) == "5555"

#24 test undo\redo concatenare string
    lista = []
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte =[2500.0, "concat"]
    lista = uiConcatStringDescriere(lista, undoList, redoList, obiecte)
    assert len(lista) == 2
    assert getDescriere(getById(1, lista)) == "vizionareconcat"
    assert getDescriere(getById(2, lista)) == "workingconcat"
    lista = undo(lista, undoList, redoList)
    assert getDescriere(getById(1, lista)) == "vizionare"
    assert getDescriere(getById(2, lista)) == "working"
    lista = redo(lista, undoList, redoList)
    assert getDescriere(getById(1, lista)) == "vizionareconcat"
    assert getDescriere(getById(2, lista)) == "workingconcat"

#25 test undo\redo ordonare dupa pret achizitie
    lista = []
    obiecte = [1, "tv", "vizionare", 5000.0, "1111"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [2, "laptop", "working", 9000.0, "2222"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    obiecte = [3, "telefon", "socializare", 4500.0, "3333"]
    lista = uiAdaugareInventar(lista, undoList, redoList, obiecte)
    lista = uiOrdonareDupaPretAchzitie(lista, undoList, redoList)
    assert getId(lista[0]) == 3
    assert getId(lista[1]) == 1
    assert getId(lista[2]) ==2
    lista = undo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getId(lista[2]) == 3
    lista = redo(lista, undoList, redoList)
    assert getId(lista[0]) == 3
    assert getId(lista[1]) == 1
    assert getId(lista[2]) ==2