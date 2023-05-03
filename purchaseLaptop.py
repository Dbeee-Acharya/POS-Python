import decorations, datetime, operations

def purchaseLaptopMain():
    '''
    Asks the user for the laptop sku of the laptop to buy, If sku exists only quantity is increased else other information is asked
    Writes over the txt file with updated quantity using a for loop
    '''

    while True:
        operations.display()

        laptopList = operations.getLaptopStock()  # get the current laptop stock
        skuList = operations.getLaptopSKU()  # get the list of laptop sku
        skuList = skuList.replace(" ", "")  # removing spaces from sku list
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

        while True:
            print("Please enter the laptop details\n")
            laptopSKU = operations.getUserInput_String("Stock Keeping Unit: ")

            if laptopSKU in skuList:
                print("\nLaptop already in inventory")
                inInventory = True
            else:
                print(decorations.decorationDash())
                print("Adding a new Laptop, please enter the details\n")
                laptopCompany = operations.getUserInput_String("Company: ")
                laptopModel = operations.getUserInput_String("Model: ")
                laptopProcessor = operations.getUserInput_String("Processor: ")
                laptopGraphics = operations.getUserInput_String("Graphics: ")
                laptopRam = operations.getUserInput_Int("Ram: ")
                laptopRam = str(laptopRam) + " GB"
                laptopStorage = operations.getUserInput_Int("Storage: ")
                laptopStorage = str(laptopStorage) + " GB"
                print(decorations.decorationDash())
            
            if(inInventory):
                laptopIndex = skuList.index(laptopSKU)
                laptopQuantity = operations.getUserInput_Int("Enter the quantity: ")
                
                laptopList[laptopIndex][-1] = " " + str(int(laptopList[laptopIndex][-1]) + laptopQuantity)
            else:
                laptopQuantity = operations.getUserInput_String("Enter the quantity: ")
                newLaptop = [laptopSKU, laptopCompany, laptopModel, laptopProcessor, laptopGraphics, laptopRam, laptopStorage, laptopQuantity]
                laptopList.append(newLaptop)

            file = open("laptop.txt","w")
        
            for i in range(len(laptopList)):
                if i == len(laptopList) - 1:
                    file.write(laptopList[i][0] + "," + laptopList[i][1] + "," + laptopList[i][2] + "," + laptopList[i][3] + "," + laptopList[i][4] + "," + laptopList[i][5]
                                + "," + laptopList[i][6] + "," + laptopList[i][7] + "," + laptopList[i][8])
                    continue
                file.write(laptopList[i][0] + "," + laptopList[i][1] + "," + laptopList[i][2] + "," + laptopList[i][3] + "," + laptopList[i][4] + "," + laptopList[i][5]
                            + "," + laptopList[i][6] + "," + laptopList[i][7] + "," + str(laptopList[i][8]) + "\n")    
            file.close()

            print(decorations.decorationDash())
            buyMore = operations.getUserInput_String("Do you want to buy more?(yes/any other key to cancel): ")
            print(decorations.decorationDash())
            buyMore = buyMore.lower()

            if buyMore != "yes":
                break

        return