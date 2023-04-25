# this module calculates the required space for different strings


# Takes the total length string and the string to write and returns the number of spaces needed
def singleString(totalString, stringToWrite):
    spaces = round((len(totalString) - len(stringToWrite))/2)
    return (" " * spaces + stringToWrite)


#  Takes a 2d array and finds the required spaces after each word in an array
def stockDisplaySpace(stock):
    spaceRequired = []

    for i in range(len(stock[0])):
        maxLenString = len(stock[0][0])
        for j in range(len(stock)):
            if maxLenString < len((stock[j][i])):
                maxLenString = len(stock[j][i])

        spaceRequired.append(maxLenString)

    return spaceRequired
