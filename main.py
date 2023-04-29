# Python coursework dibbeshwor acharya

import decorations  # Decorations
import operations # all the required operations 

# Welcome screen section
def welcomeScreenMain():
    print("\n")
    print(decorations.decorationTilde())
    print(decorations.decorationDash())
    print(operations.singleString(decorations.decorationDash(), "Laptop Sales/Purchase"))
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
        userChoice = operations.getUserInput_Int()

        if userChoice < 1 or userChoice > 4:
            print("\nSelection Invalid, please try again!\n")
            print(decorations.decorationDash())
            continue

        break

    if userChoice == 1:
        operations.getLaptopStock()
    elif userChoice == 2:
        exit()
    elif userChoice == 3:
        operations.display()

        welcomeScreenMain()  # calls the main screen again
    else:
        exit("\nProgram Closed\n")


welcomeScreenMain()
