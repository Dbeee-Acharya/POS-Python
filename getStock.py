# This module returns the laptopp stock or stock details as invoked by the user


def getLaptopStock():
    # funciton to return laptop stock
    laptopFile = open("laptop.txt", "r")
    # laptopDataDictionary = {}
    laptopFileArray = []

    for laptops in laptopFile:
        laptops = laptops.replace("\n", "").split(",")
        laptopFileArray.append(laptops)

    laptopFile.close()

    return laptopFileArray
