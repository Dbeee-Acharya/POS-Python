# This module returns the laptopp stock or stock details as invoked by the user


def getLaptopStock():
    # funciton to return laptop stock
    laptopFile = open("laptop.txt", "r")
    # laptopDataDictionary = {}
    laptopFileArray = []

    for laptops in laptopFile:
        laptops.replace("\n", "")
        laptopFileArray.append(laptops)

    laptopFile.close()

    '''for laptops in laptopData:
        laptops = laptops.replace("\n", "")
        laptopDataDictionary.update({laptopID: laptops.split(",")})
        laptopID += 1
    laptopData.close()'''

    return laptopFileArray
