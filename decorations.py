'''
This module contains all the decorations used in the program
'''
import operations


def decorationStar():
    '''Returns the specified number of star(astrict)'''
    star = "*"
    return star * 170


def decorationDash():
    '''Returns the specified number of dashes'''
    dash = "-"
    return dash * 170


def decorationTilde():
    '''Returns the specified number of tilde(~)'''
    tilde = "~"
    return tilde * 170


def headerDisplay():
    '''Returns the header for displaying stock after calculating the required spaces between the headers by calling the stockDisplaySpace method'''
    currentStockSpace = operations.stockDisplaySpace(operations.getLaptopStock())  # storing the space required for current stock in an array
    defaultSpace = " "

    headers = ["I.D.", "SKU", "Company", "Model", "Processor", "GPU", "RAM", "Storage", "Price", "Stock"]
    header = "| " + headers[0]  # initializing a string to store the final header

    # This loops over the items in header and adds the required spaces after it then concatenates it to the header string
    for i in range(1, len(headers)):
        header += "| " + headers[i] + ((currentStockSpace[i-1] - len(headers[i])) * " ") + defaultSpace

    return header
