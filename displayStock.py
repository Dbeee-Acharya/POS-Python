# This module organizes the stock

import decorations
import getStock
import spaceCalculation


def display():

    serialNumber = 1
    currentStock = getStock.getLaptopStock()
    requiredSpaces = spaceCalculation.stockDisplaySpace(currentStock)

    print("\n")
    print(decorations.decorationDash())
    print(decorations.decorationStar())

    print(decorations.headerDisplay())
    print(decorations.decorationDash())
    print(currentStock)
    print(decorations.decorationDash())

    print(decorations.decorationStar())
    input("Press any key to get back to the main screen")  # waiting for user input 
