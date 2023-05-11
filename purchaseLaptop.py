import  datetime, operations

def purchaseLaptopMain():
    '''
    Asks the user for the laptop sku of the laptop to buy, If sku exists only quantity is increased else other information is asked
    Writes over the txt file with updated quantity using a for loop 
    '''
    laptopsAdded = []

    while True:
        operations.display()

        laptopList = operations.getLaptopStock()  # get the current laptop stock
        skuListGet = operations.getLaptopSKU()  # get the list of laptop sku
        skuList = []

        for items in skuListGet:
            items = items.replace(" ", "")
            skuList.append(items)  # removing spaces from sku list

        inInventory = False  # to check if sku already exists

        # initializing variables
        laptopSKU = ""
        laptopCompany = ""
        laptopModel = ""
        laptopProcessor = ""
        laptopGraphics = ""
        laptopRam = 0
        laptopStorage = 0
        laptopQuantity = 0
        price = 0
        
        addNew = operations.getUserInput_String("Do you want to add a new laptop? (yes / anything else): ").lower()

        if addNew != "yes":
            while True:
                laptopIndex = operations.getUserInput_Int("Index of laptop you want to add: ") - 1

                if laptopIndex < 0 or laptopIndex > len(laptopList) - 1:
                    print("\n Invalid Input")
                    print(operations.decorationDash())
                    continue

                laptopQuantity = operations.getUserInput_Int("Enter the quantity: ")
                price = operations.getUserInput_Int("Price of the laptop: ")
                
                laptopList[laptopIndex][-1] = " " + str(int(laptopList[laptopIndex][-1]) + laptopQuantity)
                laptopsAdded.append([laptopList[laptopIndex][2].replace(" ", ""), str(laptopQuantity), str(price)])
                break
        else:
            print("Please enter the laptop details\n")
            laptopSKU = operations.getUserInput_String("Stock Keeping Unit: ")

            laptopCompany = operations.getUserInput_String("Company: ") + " "
            laptopModel = operations.getUserInput_String("Model: ") + " "
            laptopProcessor = operations.getUserInput_String("Processor: ") + " "
            laptopGraphics = operations.getUserInput_String("Graphics: ") + " "
            laptopRam = operations.getUserInput_Int("Ram: ") 
            laptopRam = str(laptopRam) + " GB"  + " "
            laptopStorage = operations.getUserInput_Int("Storage: ")
            laptopStorage = str(laptopStorage) + " GB" + " "
            print(operations.decorationDash())
            laptopPrice = operations.getUserInput_Int("Enter the price: ")
            laptopPrice = str(laptopPrice) + " "
            laptopQuantity = operations.getUserInput_Int("Enter the quantity: ")
            laptopQuantity = str(laptopQuantity)
            newLaptop = [laptopSKU, laptopCompany, laptopModel, laptopProcessor, laptopGraphics, laptopRam, laptopStorage, laptopPrice, laptopQuantity]
            laptopList.append(newLaptop)
            laptopsAdded.append([laptopModel.replace("  ", ""), str(laptopQuantity), str(price)])

        updateQuantity(laptopList)
        

        print(operations.decorationDash())
        buyMore = operations.getUserInput_String("Do you want to buy more?(yes/any other key to cancel): ")
        print(operations.decorationDash())
        buyMore = buyMore.lower()

        if buyMore != "yes":
            break
    
    print(generateBill(laptopsAdded))        
    return


def updateQuantity(List):
    '''
    This function takes the current laptop stock as a 2D array and updates the txt file according
    to the user purchase from distributor
    '''

    file = open("laptop.txt","w")
    
    for i in range(len(List)):
        if i == len(List) - 1:
            file.write(",".join(List[i]))
            continue
        file.write(",".join(List[i]) + "\n")
         
    file.close()

    return


def generateBill(laptops):
    '''
    Takes one parameters, a 2d array containing details about the laptops added from the distributor
    generates a txt bill file and returns the same bill file in string format
    '''

    dateAndTime = datetime.datetime.now()

    distributorName = operations.getUserInput_String("Distributor Name: ")
    distributorName = distributorName.lower()
    distributorPhone = operations.getUserInput_Int("Phone Number: ")
    distributorPhone = str(distributorPhone)
    summary = ""


    try:
        billID = distributorName + "_" + str(dateAndTime).replace(" ", "_").replace(":", "_") + "-" +  "-" +  str(distributorPhone)
    except ValueError:
        print("\n You are trying to concatenate integer with a string")
    
    bill = open("./bills/"+billID + "_distributor" + ".txt", "w")

    
    bill.write(operations.decorationTilde() + "\n")
    bill.write(operations.decorationDash() + "\n")
    bill.write(str(dateAndTime) + "\n")
    bill.write("Laptop Purchase Bill \n")
    bill.write(operations.decorationDash() + "\n")
    bill.write("Generic Laptop Shop\n")
    bill.write("Lagankhel, Lalitpur\n")
    bill.write(operations.decorationTilde() + "\n")
    bill.write(operations.decorationDash() + "\n")
    bill.write("Name: " + distributorName + "\n")
    bill.write("Phone: " + str(distributorPhone) + "\n")
    bill.write(operations.decorationDash() + "\n")
    bill.write("S.N. \t | Model \t | Quantity \t | Price \t | Total\n")
    summary += ("S.N. \t | Model \t | Quantity \t | Price \t | Total\n")
    bill.write(operations.decorationDash() + "\n")


    totalPrice = 0
  

    for i in range(len(laptops)):
        bill.write(
            "| " + str(i + 1) + "\t| " + str(laptops[i][0]) + "\t| "
            + str(laptops[i][1]) + "\t| "
            + str(laptops[i][2]) + "\t| " 
            + str(int(laptops[i][1]) * int(laptops[i][2])) + "\n")
        totalPrice += int(laptops[i][1]) * int(laptops[i][2])
    
    for i in range(len(laptops)):
        summary += (
            "| " + str(i + 1) + "\t| " + str(laptops[i][0]) + "\t| "
            + str(laptops[i][1]) + "\t| " + str(laptops[i][2]) + "\t| " + str(int(laptops[i][1]) * int(laptops[1][2])) + "\n")

    bill.write(operations.decorationTilde() + "\n")
    bill.write(operations.decorationDash() + "\n")

    summary += (operations.decorationDash() + "\n")
    
    
    bill.write("Price of laptop: Rs." + str(totalPrice) + "\n")
    bill.write("Taxable Amount: Rs." + str(totalPrice) + "\n")
    vatAmount = float((totalPrice) * 13/100)
    bill.write("13% Vat Amount: Rs." + str(vatAmount) + "\n")
    bill.write("Grand Total: Rs." + str(vatAmount + totalPrice) +"\n")

    summary += ("Price of laptop: Rs." + str(totalPrice) + "\n")
    summary += ("Taxable Amount: Rs." + str(totalPrice) + "\n")
    vatAmount = float((totalPrice) * 13/100)
    summary += ("13% Vat Amount: Rs." + str(vatAmount) + "\n")
    summary += ("Grand Total: Rs." + str(vatAmount + totalPrice) +"\n")
    

    bill.write(operations.decorationDash() + "\n")
    bill.write(operations.decorationTilde())

    bill.close()
    print("\nBill generated Successfully!\n")
    print(operations.decorationStar())
    print(operations.decorationDash())
    
    return summary
