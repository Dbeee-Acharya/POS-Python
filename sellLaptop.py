import decorations, operations, datetime


def sellLaptopMain():
    while True:
        laptopsBoughtIndex = []
        quantityBought = []
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
            if (confirmToBuy == "yes" or confirmToBuy == "no"):
                if confirmToBuy == "yes":
                    print("yes")
                    decreaseStock(laptopToBuy, quantityOfLaptop, laptopList)
                    laptopsBoughtIndex.append(laptopToBuy)
                    quantityBought.append(quantityOfLaptop)
                    print(f" {quantityOfLaptop} pieces of {laptopList[laptopToBuy][0]} for ${quantityOfLaptop * int(laptopList[laptopToBuy][7])} added to bill")
                    # generateBill(laptopToBuy, quantityOfLaptop, laptopList)
                break
            else: 
                print("\n Operation Cancelled")
                break
            
        print(decorations.decorationDash())
        buyMore = operations.getUserInput_String("Do you want to buy more?:(yes/any other key to cancel)")
        print(decorations.decorationDash())
        buyMore = buyMore.lower()

        if buyMore != "yes":
            break

    generateBill(laptopsBoughtIndex, quantityBought, laptopList)

def decreaseStock(laptop, quantity, list):
    file = open("laptop.txt","w")
    
    for i in range(len(list)):
        if i == laptop:
            file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
                        + "," + list[i][6] + "," + list[i][7] + ", " + str(int(list[i][8]) - quantity) + "\n")
            continue
        elif i == len(list) - 1:
            file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
                         + "," + list[i][6] + "," + list[i][7] + "," + list[i][8])
            continue
        file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
                    + "," + list[i][6] + "," + list[i][7] + "," + list[i][8] + "\n")
        
    file.close()
    return

def generateBill(laptopIndex, quantity, list):
    dateAndTime = datetime.datetime.now()

    customerName = operations.getUserInput_String("Customer Name: ")
    customerName = customerName.lower()
    customerPhone = operations.getUserInput_Int("Phone Number: ")
    customerPhone = str(customerPhone)

    while True:
        wantShipping = operations.getUserInput_String("Do you want shipping for Rs.500?(yes/no)")
        wantShipping = wantShipping.lower() 
        if wantShipping != "yes" or wantShipping != "no":
            print("\n")
            print("Please type yes or no")
            print(decorations.decorationDash())

        if wantShipping == "yes":
            wantShipping = True
        else:
            wantShipping = False
        break
    try:
        billID = str(dateAndTime).replace(" ", "_").replace(":", "_") + "-" + customerName + "-" +  str(customerPhone)
    except ValueError:
        print("\n You are trying to concatenate integer with a string")
    
    bill = open(str(billID) + ".txt", "w")

    
    bill.write(decorations.decorationTilde() + "\n")
    bill.write(decorations.decorationDash() + "\n")
    bill.write(str(dateAndTime) + "\n")
    bill.write("Laptop Purchase Bill \n")
    bill.write(decorations.decorationDash() + "\n")
    bill.write("Generic Laptop Shop\n")
    bill.write("Lagankhel, Lalitpur\n")
    bill.write(decorations.decorationTilde() + "\n")
    bill.write(decorations.decorationDash() + "\n")
    bill.write("Name: " + customerName + "\n")
    bill.write("Phone: " + str(customerPhone) + "\n")
    bill.write(decorations.decorationDash() + "\n")
    bill.write("S.N. \t | Company \t | Model \t | Quantity \t | Price \t | Total\n")
    bill.write(decorations.decorationDash() + "\n")


    totalPrice = 0

    for i in range(len(laptopIndex)):
        bill.append(
            "| " + str(i + 1) + " | " + str(list[laptopIndex[i]][1]) + " | "
            + str(list[laptopIndex[i]][2]) + " | " + str(quantity[i])
            + " | " + str(list[laptopIndex[i]][7]) + " | " + str((int(list[laptopIndex[i]][7]) * int(quantity[i]))) + "\n")
        totalPrice += int(list[laptopIndex[i]][7]) * int(quantity[i])

    bill.write(decorations.decorationTilde() + "\n")
    bill.write(decorations.decorationDash() + "\n")
    
    if wantShipping:
        wantShipping = 500
    else:
        wantShipping = 0
    
    bill.write("Shipping Cost: Rs." + str(wantShipping) + "\n")
    bill.write("Price of laptop: Rs." + str(totalPrice) + "\n")
    bill.write("Grand Total: Rs." + str(totalPrice + wantShipping) + "\n")

    bill.write(decorations.decorationDash() + "\n")
    bill.write(decorations.decorationTilde())

    bill.close()
    print("\nBill generated Successfully!")
    input("\npress any key to get back to the main screen")
    
    return
        