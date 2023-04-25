# Python coursework dibbeshwor acharya

import decorations  # Decorations
import getStock  # Module that returns the stock details
import userInput  # module that handles userInput
import spaceCalculation  # module to calculate the required space
import displayStock  # module to display the stock in an orgonized manner


# Welcome screen section
def welcomeScreenMain():
    print("\n")
    print(decorations.decorationTilde())
    print(decorations.decorationDash())
    print(spaceCalculation.singleString(decorations.decorationDash(), "Laptop Sales/Purchase"))
    print(decorations.decorationDash())
    print(decorations.decorationTilde())

    print("Please choose the required option")
    print("\n")

    print("1. Laptop Sales")
    print("2. Laptop Purcahse")
    print("3. Current Stock")
    print("4. Exit the program")
    print(decorations.decorationDash())
    print(decorations.decorationStar())
    print("\n")

    while True:
        userChoice = userInput.getUserInput_Int()

        if userChoice < 1 or userChoice > 4:
            print("\nSelection Invalid, please try again!\n")
            print(decorations.decorationDash())
            continue

        break

    if userChoice == 1:
        getStock.getLaptopStock()
    elif userChoice == 2:
        exit()
    elif userChoice == 3:
        displayStock.display()

        welcomeScreenMain()  # calls the main screen again
    else:
        exit("\nProgram Closed\n")


welcomeScreenMain()
