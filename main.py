from Tests.testAll import runAllTests
from UI.command_line_console import main_line
from UI.console import runMenu


def main():
    runAllTests()
    #runMenu([])
    main_line([])

if __name__ == '__main__':
    main()