from Tests.testCRUD import testAdaugaInventar
from Tests.testDomain import testInventar
from Tests.testFunctionalitati import testModificareLocatieInventare


def runAllTests():
    testInventar()
    testAdaugaInventar()
    testModificareLocatieInventare()