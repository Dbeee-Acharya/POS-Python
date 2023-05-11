'''
This is the main module, which calls every other required module as per the user choice
This module has one function welcomeScreenMain(): which is looped until the user exits the 
program
'''

import operations # all the required operations 
import sellLaptop # all functions relating to sales of laptop
import purchaseLaptop # all the functions relating to the purchase of laptop

# Welcome screen section

def welcomeScreenMain():
    '''This method is run at the very beginning, it prints the required welcome message and asks the user for their choice. This method loops until the user exits the program'''
    while True:
        print("\n")
        print(operations.decorationTilde())
        print(operations.decorationDash())
        print(operations.singleString(operations.decorationDash(), "Laptop Sales/Purchase"))
        print(operations.decorationDash())
        print(operations.decorationTilde())

        print("Please choose the required option")
        print("\n")

        print("1. Laptop Sales")
        print("2. Laptop Purchase")
        print("3. Current Stock")
        print("4. Exit the program")
        print(operations.decorationDash())
        print(operations.decorationStar())
        print("\n")

        while True:
            userChoice = operations.getUserInput_Int("Your Choice: ")  # Asking the user which action they want to perform

            # Input validation for the available choice
            if userChoice < 1 or userChoice > 4:
                print("\nSelection Invalid, please try again!\n")
                print(operations.decorationDash())
                continue

            break
        
        if userChoice == 1:
            print(operations.decorationDash())
            operations.display()  # Calling the main Display method which displays the available stock 

            sellLaptop.sellLaptopMain()  # Calling the sell method which decreases stock and generates bill as required by the user

            print(operations.decorationTilde())
            print(operations.decorationDash())
                
        elif userChoice == 2:
            purchaseLaptop.purchaseLaptopMain()  # calling the purchase function which increases stock or adds new stock as per requirement
        elif userChoice == 3:
            operations.display()
            input("Press any key to get back to the main screen")  # waiting for user input before looping again
            welcomeScreenMain()  # calls the main screen again

        else:
            exit("\nProgram Closed\n")  # exits the program with this message


welcomeScreenMain()
