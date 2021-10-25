from Tests.testCRUD import testAdaugaInventar, testGetById, testModificaInventar, testStergeInventar
from Tests.testDomain import testInventar
from Tests.testFunctionalitati import testModificareLocatieInventare


def runAllTests():
    testInventar()
    testAdaugaInventar()
    testModificareLocatieInventare()
    testStergeInventar()
    testGetById()
    testModificaInventar()