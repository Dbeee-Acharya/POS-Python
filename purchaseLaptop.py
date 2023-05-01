import decorations, datetime, operations

def purchaseLaptopMain():
    laptopList = operations.getLaptopStock()
    skuList = operations.getLaptopSKU()
    while True:
        print("Please enter the laptop details\n")
        laptopSKU = operations.getUserInput_String("Stock Keeping Unit: ")

        if laptopSKU in skuList:
            print("Laptop already in inventory")
            inInventory = True
        else:
            laptopCompany = operations.getUserInput_String("Company: ")
            laptopModel = operations.getUserInput_String("Model: ")
            laptopProcessor = operations.getUserInput_String("Processor: ")
            laptopGraphics = operations.getUserInput_String("Graphics: ")
            laptopRam = operations.getUserInput_Int("Ram: ")
            laptopRam = str(laptopRam) + " GB"
            laptopStorage = operations.getUserInput_Int("Storage: ")
            laptopStorage = str(laptopStorage) + " GB"
    return

purchaseLaptopMain()