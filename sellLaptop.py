'''
This function is called when the user wants to sell laptop to the client
'''

import decorations, operations, datetime


def sellLaptopMain():
    '''
    Asks user for which laptop to sell, which is then input validated
    Then calls the update quantity function which updates the quantity from the txt file
    Then Generates a bill using the bill generation function
    '''
    laptopsBoughtIndex = []
    quantityBought = []

    while True:
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
        print(f"Are you sure you want to buy {quantityOfLaptop} pieces of {laptopList[laptopToBuy][2]} for ${quantityOfLaptop * int(laptopList[laptopToBuy][7])}")

        while True:
            confirmToBuy = (operations.getUserInput_String("Yes/No?: "))
            if (confirmToBuy == "yes" or confirmToBuy == "no"):
                if confirmToBuy == "yes":
                    print("yes")
                    decreaseStock(laptopToBuy, quantityOfLaptop, laptopList)
                    laptopsBoughtIndex.append(laptopToBuy)
                    quantityBought.append(quantityOfLaptop)
                    print(f" {quantityOfLaptop} pieces of {laptopList[laptopToBuy][2]} for ${quantityOfLaptop * int(laptopList[laptopToBuy][7])} added to bill")
                    # generateBill(laptopToBuy, quantityOfLaptop, laptopList)
                break
            else: 
                print("\n Operation Cancelled")
                break
            
        print(decorations.decorationDash())
        buyMore = operations.getUserInput_String("Do you want to buy more?(yes/any other key to cancel): ")
        print(decorations.decorationDash())
        buyMore = buyMore.lower()

        if buyMore != "yes":
            break

    generateBill(laptopsBoughtIndex, quantityBought, laptopList)
    print(summaryOfSales(laptopsBoughtIndex, quantityBought, laptopList))
    input("press any key to continue")
    return

def decreaseStock(laptop, quantity, list):
    '''
    Takes three parameters, laptops bought a list containing indexes of the laptop bought by the user
    quantity, a list containing the quantity bought for the respective index of laptops list
    list, a 2d list containing the current laptop stock
    Loops and writes the file
    '''

    file = open("laptop.txt","w")
    
    for i in range(len(list)):
        if i == laptop:
            # file.write(",".join(list[i]) + "\n")
            file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
                        + "," + list[i][6] + "," + list[i][7] + ", " + str(int(list[i][8]) - quantity) + "\n")
            continue
        elif i == len(list) - 1:
            file.write(",".join(list[i]))
            # file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
            #              + "," + list[i][6] + "," + list[i][7] + "," + list[i][8])
            continue
        file.write(",".join(list[i]) + "\n")
        # file.write(list[i][0] + "," + list[i][1] + "," + list[i][2] + "," + list[i][3] + "," + list[i][4] + "," + list[i][5]
        #             + "," + list[i][6] + "," + list[i][7] + "," + list[i][8] + "\n")
        
    file.close()
    return


def generateBill(laptopIndex, quantity, list):
    '''
    Takes Three parameters, LaptopIndex is a list containing the indexes of laptops bought
    quantity is a list containing the quantity bought of the respective index of laptopIndex
    list is a 2d list containing the current stock
    Bill is generated and stored in the bill folder
    '''

    dateAndTime = datetime.datetime.now()

    customerName = operations.getUserInput_String("Customer Name: ")
    customerName = customerName.lower()
    customerPhone = operations.getUserInput_Int("Phone Number: ")
    customerPhone = str(customerPhone)

    while True:
        wantShipping = operations.getUserInput_String("Do you want shipping for Rs.500?(yes/no): ")
        wantShipping = wantShipping.lower() 
        if wantShipping != "yes" and wantShipping != "no":
            print("\n")
            print("Please type yes or no")
            print(decorations.decorationDash())

        if wantShipping == "yes":
            wantShipping = True
        else:
            wantShipping = False
        break
    try:
        billID = customerName + "_" + str(dateAndTime).replace(" ", "_").replace(":", "_") + "-" +  "-" +  str(customerPhone)
    except ValueError:
        print("\n You are trying to concatenate integer with a string")
    
    bill = open("./bills/"+billID + ".txt", "w")

    
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
        bill.write(
            "| " + str(i + 1) + "\t| " + str(list[laptopIndex[i]][1]) + "\t| "
            + str(list[laptopIndex[i]][2]) + "\t| " + str(quantity[i])
            + "\t| " + str(list[laptopIndex[i]][7]) + "\t| " + str((int(list[laptopIndex[i]][7]) * int(quantity[i]))) + "\n")
        totalPrice += int(list[laptopIndex[i]][7]) * int(quantity[i])

    bill.write(decorations.decorationTilde() + "\n")
    bill.write(decorations.decorationDash() + "\n")
    
    if wantShipping:
        wantShipping = 500
    else:
        wantShipping = 0
    
    bill.write("Shipping Cost: Rs." + str(wantShipping) + "\n")
    bill.write("Price of laptop: Rs." + str(totalPrice) + "\n")
    bill.write("Taxable Amount: Rs." + str(totalPrice + wantShipping) + "\n")
    vatAmount = float((totalPrice + wantShipping) * 13/100)
    bill.write("13% Vat Amount: Rs." + str(vatAmount) + "\n")
    bill.write("Grand Total: Rs." + str(vatAmount + totalPrice + wantShipping) +"\n")
    

    bill.write(decorations.decorationDash() + "\n")
    bill.write(decorations.decorationTilde())

    bill.close()
    print("\nBill generated Successfully!\n")
    print(decorations.decorationStar())
    print(decorations.decorationDash())
    
    return


def summaryOfSales(laptopIndex, quantity, list):
    '''
    This function takes the index of laptops bought, quantity bought and a list containing the current stock
    and returns a summary of the transaction carried out by the user stored in a string
    '''
    summary = ""
    totalPrice = 0

    summary += "Summary of bill \n"
    summary += decorations.decorationStar() + "\n" + decorations.decorationDash() + "\n"
    summary += "S.N|\t|Product |\t|Quantity |\t|Price   |\t\t| Total\n"

    for i in range(len(laptopIndex)):
        summary += (
            "| " + str(i+1) + "\t| " + str(list[laptopIndex[i]][1]) + "\t| "
            + str(list[laptopIndex[i]][2]) + "\t| " + str(quantity[i])
            + "\t| " + str(list[laptopIndex[i]][7]) + "\t| " + str((int(list[laptopIndex[i]][7]) * int(quantity[i]))) + "\n\n")
        totalPrice += int(list[laptopIndex[i]][7]) * int(quantity[i])

    summary += decorations.decorationDash() + "\n"
    summary += ("Price of laptop: Rs." + str(totalPrice) + "\n")
    summary += ("Taxable Amount: Rs." + str(totalPrice) + "\n")
    vatAmount = float((totalPrice) * 13/100)
    summary += ("13% Vat Amount: Rs." + str(vatAmount) + "\n")
    summary += ("Grand Total: Rs." + str(vatAmount + totalPrice) +"\n")
    
    # for index in laptopIndex:
    #     summary += str(sn) + " | " + list[index][2] + (" " * (15 - len(list[index][2]))) + "| " + str(quantity[index]) + (" " *(5 - len(str(quantity[index])))) + str() "\n"
    #     sn += 1
    
    summary += decorations.decorationDash() 
    return summary
    


        