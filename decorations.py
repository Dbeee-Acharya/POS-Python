# This module contains all the decorations used in the program
import operations


def decorationStar():
    star = "*"
    return star * 170


def decorationDash():
    dash = "-"
    return dash * 170


def decorationTilde():
    tilde = "~"
    return tilde * 170


def headerDisplay():
    currentStockSpace = operations.stockDisplaySpace(operations.getLaptopStock())  # storing the space required for current stock in an array
    defaultSpace = " "

    headers = ["I.D.", "SKU", "Company", "Model", "Processor", "GPU", "RAM", "Storage", "Price", "Stock"]
    header = "| " + headers[0]

    for i in range(1, len(headers)):
        header += "| " + headers[i] + ((currentStockSpace[i-1] - len(headers[i])) * " ") + defaultSpace

    return header
