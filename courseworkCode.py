# Python coursework dibbeshwor acharya

def decorationStar():
    return ("**********************************************************************")


def decorationDash():
    return ("----------------------------------------------------------------------")


# Welcome screen section
print(decorationStar())
print("\t\t\tLaptop Sales/Purchase")
print(decorationStar())
print(decorationDash())

print("Please choose the required option")
print("\n")

print("1. Laptop Sales")
print("2. Laptop Purcahse")
print("3. Exit the program")
print(decorationDash())
print(decorationStar())
print("\n")

while True:
    try:
        userChoiceWelcomeScreen = int(input("Your choice: "))
        break
    except ValueError:
        print("\nSelection Invalid, please try again!\n")
        print(decorationDash())


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
