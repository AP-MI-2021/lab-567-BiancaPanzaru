from Tests.testCRUD import testAdaugaInventar, testGetById, testModificaInventar, testStergeInventar
from Tests.testDomain import testInventar
from Tests.testFunctionalitati import testModificareLocatieInventare, testPretMax, testOrdonareDupaPretAchzitie, \
    testConcatSTringDescriere
from Tests.testUndoRedo import test_Undo_Redo


def runAllTests():
    testInventar()
    testAdaugaInventar()
    testModificareLocatieInventare()
    testConcatSTringDescriere()
    testPretMax()
    testOrdonareDupaPretAchzitie()
    testStergeInventar()
    testGetById()
    testModificaInventar()
    test_Undo_Redo()