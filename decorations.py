# This module contains all the decorations used in the program
import spaceCalculation
import getStock

currentStockSpace = spaceCalculation.stockDisplaySpace(getStock.getLaptopStock())  # storing the space required for current stock in an array
defaultSpace = "   "


def decorationStar():
    star = "*"
    return star * 100


def decorationDash():
    dash = "-"
    return dash * 100


def decorationTilde():
    tilde = "~"
    return tilde * 100


def headerDisplay():
    headers = ["S.N.", "I.D.", "Company", "Model", "Processor", "GPU", "RAM", "Storage", "Price", "Stock"]
    header = "| " + headers[0] + " "

    for i in range(1, len(headers)):
        header += "| " + headers[i]  + ((currentStockSpace[i-1] - len(headers[i])) * " ") + defaultSpace

    return header
