from Tests.testCRUD import testAdaugaInventar, testGetById, testModificaInventar, testStergeInventar
from Tests.testDomain import testInventar
from Tests.testFunctionalitati import testModificareLocatieInventare, testPretMax, testOrdonareDupaPretAchzitie, \
    testConcatSTringDescriere


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