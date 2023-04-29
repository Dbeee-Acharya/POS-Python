import decorations

'''To Find the total required space for displaying informations'''

# Takes the total length string and the string to write and returns the number of spaces needed
def singleString(totalString, stringToWrite):
    spaces = round((len(totalString) - len(stringToWrite))/2)
    return (" " * spaces + stringToWrite)


#  Takes a 2d array and finds the required spaces after each word in an array
def stockDisplaySpace(stock):
    spaceRequired = []

    for i in range(len(stock[0])):
        maxLenString = len(stock[0][0])
        for j in range(len(stock)):
            if maxLenString < len((stock[j][i])):
                maxLenString = len(stock[j][i])

        spaceRequired.append(maxLenString)

    return spaceRequired

'''TO take user input with try catch'''

# Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
def getUserInput_Int():
    while True:
        try:
            userChoice = int(input("Your choice: "))
            return userChoice

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorations.decorationDash())

'''To take stock from the laptop.txt file'''

# This funciton returns the laptop stock or stock details as invoked by the user
def getLaptopStock():
    laptopFile = open("laptop.txt", "r")
    # laptopDataDictionary = {}
    laptopFileArray = []

    for laptops in laptopFile:
        laptops = laptops.replace("\n", "").split(",")
        laptopFileArray.append(laptops)

    laptopFile.close()

    return laptopFileArray

'''To display the stock'''

def display():

    serialNumber = 1  # to assign unique sn to each laptop while displaying
    currentStock = getLaptopStock()  # 2d array containing current stock of laptop is stored 
    requiredSpaces = stockDisplaySpace(currentStock)  # array of required spaces 

    defaultSpace = " "  # default distance between info while displaying

    print("\n")
    print(decorations.decorationDash())
    print(decorations.decorationStar())

    print(decorations.headerDisplay())
    print(decorations.decorationDash())

    for i in range(len(currentStock)):
        string = ""
        string += "| " + str(serialNumber) + "   "
        for j in range(len(currentStock[i])):
            string += "| " + str(currentStock[i][j]) + (" "*(requiredSpaces[j] - len(currentStock[i][j])) + defaultSpace)

        print(string)
        serialNumber += 1

    print(decorations.decorationDash())

    print(decorations.decorationStar())
    input("Press any key to get back to the main screen")  # waiting for user input 
