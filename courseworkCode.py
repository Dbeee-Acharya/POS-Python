# Python coursework dibbeshwor acharya

import sys # gives us access to variables used or maintained by the interpreter. Used in this code to call sys.exit() which closes the program


def decorationStar():
    return ("**********************************************************************")


def decorationDash():
    return ("----------------------------------------------------------------------")


# Welcome screen section
def welcomeScreenMain():
    print(decorationStar())
    print("\t\t\tLaptop Sales/Purchase")
    print(decorationStar())
    print(decorationDash())

    print("Please choose the required option")
    print("\n")

    print("1. Laptop Sales")
    print("2. Laptop Purcahse")
    print("3. Current Stock")
    print("4. Exit the program")
    print(decorationDash())
    print(decorationStar())
    print("\n")

    # Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
    while True:
        try:
            userChoiceWelcomeScreen = int(input("Your choice: "))

            if userChoiceWelcomeScreen < 1 or userChoiceWelcomeScreen > 4:
                print("\nSelection Invalid, please try again!\n")
                print(decorationDash())
                continue

            break

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorationDash())

    if userChoiceWelcomeScreen == 1:
        getLaptopStock()
    elif userChoiceWelcomeScreen == 2:
        sellLaptop()
    elif userChoiceWelcomeScreen == 3:
        getLaptopStock()
    else:
        sys.exit("\nProgram Closed\n")


def getLaptopStock():
    # funciton to return laptop stock
    laptopData = open("laptop.txt", "r")
    laptopDataDictionary = {}
    laptopArray = []

    laptops = laptopData.readlines()

    for laptop in laptops:
        laptopArray.append(laptop.replace("\n", "").split(","))

    return laptopArray


def sellLaptop():
    # to sell laptop
    return


def purchaseLaptop():
    # to purchase laptop
    return


welcomeScreenMain()
