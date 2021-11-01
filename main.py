from Tests.testAll import runAllTests
from UI.command_line_console import main_line
from UI.console import runMenu


def main():
    runAllTests()
    meniu = str(input("Scrieti ce fel de meniu doriti: clasic sau comenzi: "))
    if meniu == "clasic":
        runMenu([])
    elif meniu == "comenzi":
        main_line([])

if __name__ == '__main__':
    main()