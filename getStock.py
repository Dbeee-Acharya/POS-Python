# This module returns the laptopp stock or stock details as invoked by the user


def getLaptopStock():
    # funciton to return laptop stock
    laptopData = open("laptop.txt", "r")
    laptopDataDictionary = {}
    # laptopID = 1

    for laptops in laptopData:
        print(laptops.replace(",", ""))
        '''laptops = laptops.replace("\n", "")
        laptopDataDictionary.update({laptopID: laptops.split(",")})
        laptopID += 1'''
    laptopData.close()

    return laptopDataDictionary
