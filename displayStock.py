# This module organizes the stock

import decorations
import getStock


def display():

    serialNumber = 1

    print("\n")
    print(decorations.decorationDash())
    print(decorations.decorationStar())

    print(decorations.headerDisplay())
    print(decorations.decorationDash())
    print(getStock.getLaptopStock())
    print(decorations.decorationDash())

    print(decorations.decorationStar())
    input("Press any key to get back to the main screen")  # waiting for user input 
