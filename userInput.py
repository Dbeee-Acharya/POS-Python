# This module handles all userInput functions
import decorations.py  # for decorations


# Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
def getUserInputInt():
    while True:
        try:
            userChoice = int(input("Your choice: "))
            return userChoice

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorations.decorationDash())
