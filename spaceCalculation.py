# this module calculates the required space for different strings


# Takes the total length string and the string to write and returns the number of spaces needed
def singleString(totalString, stringToWrite):
    spaces = round((len(totalString) - len(stringToWrite))/2)
    return (" " * spaces + stringToWrite)
