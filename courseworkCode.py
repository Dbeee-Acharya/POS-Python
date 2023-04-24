# Python coursework dibbeshwor acharya


def decorationStar():
    return ("***************************************************************************")


def decorationDash():
    return ("---------------------------------------------------------------------------")


# Welcome screen section
def welcomeScreenMain():
    print("\n")
    print(decorationDash())
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

    while True:
        userChoice = getUserInputInt()

        if userChoice < 1 or userChoice > 4:
            print("\nSelection Invalid, please try again!\n")
            print(decorationDash())
            continue

        break

    if userChoice == 1:
        getLaptopStock()
    elif userChoice == 2:
        sellLaptop()
    elif userChoice == 3:
        print(decorationStar())
        print(decorationDash())

        print(getLaptopStock())
        print(decorationDash())

        print(decorationStar())
        input("Press any key to get back to the main screen")  # waiting for user input

        welcomeScreenMain()  # calls the main screen again
    else:
        exit("\nProgram Closed\n")


# Takes userInput for desired choice. Any out of bounds choice or Invalid choice is error handled
def getUserInputInt():
    while True:
        try:
            userChoice = int(input("Your choice: "))
            return userChoice

        except ValueError:
            print("\nSelection Invalid, please try again!\n")
            print(decorationDash())


def getLaptopStock():
    # funciton to return laptop stock
    laptopData = open("laptop.txt", "r")
    laptopDataDictionary = {}
    laptopID = 1

    for laptops in laptopData:
        laptops = laptops.replace("\n", "")
        laptopDataDictionary.update({laptopID: laptops.split(",")})
        laptopID += 1
    laptopData.close()

    return laptopDataDictionary


def sellLaptop():
    # to sell laptop
    return


def purchaseLaptop():
    # to purchase laptop
    return


welcomeScreenMain()
