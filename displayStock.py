# This module organizes the stock

import decorations
import getStock
import spaceCalculation


def display():

    serialNumber = 1  # to assign unique sn to each laptop while displaying
    currentStock = getStock.getLaptopStock()  # 2d array containing current stock of laptop is stored 
    requiredSpaces = spaceCalculation.stockDisplaySpace(currentStock)  # array of required spaces 

    defaultSpace = "   "  # default distance between info while displaying

    print("\n")
    print(decorations.decorationDash())
    print(decorations.decorationStar())

    print(decorations.headerDisplay())
    print(decorations.decorationDash())

    print(requiredSpaces)

    for i in range(len(currentStock)):
        string = ""
        string += "| " + str(serialNumber) + defaultSpace
        for j in range(len(currentStock[i])):
            string += "| " + str(currentStock[i][j]) + (" "*(requiredSpaces[j] - len(currentStock[i][j])) + defaultSpace)

        print(string + " |")
        serialNumber += 1

    print(decorations.decorationDash())

    print(decorations.decorationStar())
    input("Press any key to get back to the main screen")  # waiting for user input 
