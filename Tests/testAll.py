from Tests.testCRUD import testAdaugaInventar, testGetById, testModificaInventar
from Tests.testDomain import testInventar
from Tests.testFunctionalitati import testModificareLocatieInventare


def runAllTests():
    testInventar()
    testAdaugaInventar()
    testModificareLocatieInventare()
    testGetById()
    testModificaInventar()