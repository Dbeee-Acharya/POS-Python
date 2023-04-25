# This module handles all userInput functions
import decorations  # for decorations


# Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
def getUserInput_Int():
    while True:
        try:
            userChoice = int(input("Your choice: "))
            return userChoice

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorations.decorationDash())
