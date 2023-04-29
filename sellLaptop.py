import decorations, operations, datetime


def sellLaptopMain():
    laptopList = operations.getLaptopStock()
    while True:
        laptopToBuy = (operations.getUserInput_Int("\nLaptop ID: ")) -1

        if not(laptopToBuy < 0 or laptopToBuy > len(laptopList) - 1):
            break
        print(decorations.decorationDash()) 
        print("Invalid ID")
        print(decorations.decorationDash())

    print(decorations.decorationTilde())
    print(decorations.decorationDash())

    while True:
        quantityOfLaptop = operations.getUserInput_Int("Quantity of Laptop to buy: ")
        
        if not(quantityOfLaptop < 0 or quantityOfLaptop > int(laptopList[laptopToBuy][8])):
            break 
        print(decorations.decorationDash()) 
        print("Invalid quantity")
        print(decorations.decorationDash())

        print("\n")
        print(decorations.decorationTilde())
        print(decorations.decorationDash())

    print(decorations.decorationDash())
    print(f"Are you sure you want to buy {quantityOfLaptop} pieces of {laptopList[laptopToBuy][0]} for ${quantityOfLaptop * int(laptopList[laptopToBuy][7])}")

    while True:
        confirmToBuy = (operations.getUserInput_String("Yes/No?: "))
        confirmToBuy = confirmToBuy.lower()
        if (confirmToBuy == "yes" or confirmToBuy == "no"):
            if confirmToBuy == "yes":
                print("yes")
                generateBill(laptopToBuy, quantityOfLaptop)
                break
            print("\n Operation Cancelled")
            break
        print(decorations.decorationDash())
        print("please type yes or No")
        print(decorations.decorationDash())

def generateBill(laptop, quantity):
    
    return
        