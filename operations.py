

# Takes the total length string and the string to write and returns the number of spaces needed
def singleString(totalString, stringToWrite):
    '''To Find the total required space for displaying information'''
    spaces = round((len(totalString) - len(stringToWrite))/2)
    return (" " * spaces + stringToWrite)


#  Takes a 2d array and finds the required spaces after each word in an array
def stockDisplaySpace(stock):
    '''
    Takes a 2d Array containing the current stock as a parameter and finds the required space after each word.
    Finds the longest string in a column, then uses the formula (length longest string - length current string) * " " + default space
    '''
    spaceRequired = []

    # Looping over each column and finding the maximum string length which is then stored in a array
    for i in range(len(stock[0])):
        maxLenString = len(stock[0][0])
        for j in range(len(stock)):
            if maxLenString < len((stock[j][i])):
                maxLenString = len(stock[j][i])

        spaceRequired.append(maxLenString)

    return spaceRequired


# Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
def getUserInput_Int(message):
    '''
    This function takes message as the parameter, which is displayed while asking for input
    The try catch block validates if the input is int or not, and loops the function until the user provides the required input
    Returns the userInput
    '''
    while True:
        try:
            userChoice = int(input(message))
            return userChoice

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorationDash())


# userinput for string
def getUserInput_String(message):
        '''Takes a String input and returns it in all lower case for easier condition checking'''
        userChoice = input(message)
        return userChoice.lower()



# This function returns the laptop stock or stock details as invoked by the user
def getLaptopStock():
    '''
    Converts each line into an array and appends it to the laptopFileArray
    The 2d array is then returned
    '''

    laptopFile = open("laptop.txt", "r")
    # laptopDataDictionary = {}
    laptopFileArray = []

    for laptops in laptopFile:
        laptops = laptops.replace("\n", "").split(",")
        laptopFileArray.append(laptops)

    laptopFile.close()

    return laptopFileArray



def getLaptopPrice():
    '''Returns an array containing all the prices of laptops of the respective index'''

    laptopList = getLaptopStock()
    priceList = []

    for laptops in laptopList:
        priceList.append(laptops[7])

    return priceList


# To get the SKU of laptop
def getLaptopSKU():
    '''Returns an array containing the SKU of laptops of their respective index'''
    laptopList = getLaptopStock()
    skuList = []

    for laptops in laptopList:
        skuList.append(laptops[0].lower())

    return skuList


def display():
    '''Displays the stock after calculating the required spaces using the requiredSpaces function'''

    serialNumber = 1  # to assign unique sn to each laptop while displaying
    currentStock = getLaptopStock()  # 2d array containing current stock of laptop is stored 
    requiredSpaces = stockDisplaySpace(currentStock)  # array of required spaces 

    defaultSpace = " "  # default distance between info while displaying

    print("\n")
    print(decorationDash())
    print(decorationStar())

    print(headerDisplay())
    print(decorationDash())

    for i in range(len(currentStock)):
        string = ""
        string += "| " + str(serialNumber) + "   "
        for j in range(len(currentStock[i])):
            string += "| " + str(currentStock[i][j]) + (" "*(requiredSpaces[j] - len(currentStock[i][j])) + defaultSpace)

        print(string)
        serialNumber += 1

    print(decorationDash())
    print(decorationStar())
    return


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
    currentStockSpace = stockDisplaySpace(getLaptopStock())  # storing the space required for current stock in an array
    defaultSpace = " "

    headers = ["I.D.", "SKU", "Company", "Model", "Processor", "GPU", "RAM", "Storage", "Price", "Stock"]
    header = "| " + headers[0]  # initializing a string to store the final header

    # This loops over the items in header and adds the required spaces after it then concatenates it to the header string
    for i in range(1, len(headers)):
        header += "| " + headers[i] + ((currentStockSpace[i-1] - len(headers[i])) * " ") + defaultSpace

    return header
