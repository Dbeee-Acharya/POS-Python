# Python coursework dibbeshwor acharya

import decorations  # Decorations
import operations # all the required operations 
import sellLaptop # all functions relating to sales of laptop

# Welcome screen section

def welcomeScreenMain():
    while True:
        print("\n")
        print(decorations.decorationTilde())
        print(decorations.decorationDash())
        print(operations.singleString(decorations.decorationDash(), "Laptop Sales/Purchase"))
        print(decorations.decorationDash())
        print(decorations.decorationTilde())

        print("Please choose the required option")
        print("\n")

        print("1. Laptop Sales")
        print("2. Laptop Purcahse")
        print("3. Current Stock")
        print("4. Exit the program")
        print(decorations.decorationDash())
        print(decorations.decorationStar())
        print("\n")

        while True:
            userChoice = operations.getUserInput_Int("Your Choice: ")

            if userChoice < 1 or userChoice > 4:
                print("\nSelection Invalid, please try again!\n")
                print(decorations.decorationDash())
                continue

            break
        
        if userChoice == 1:
            print(decorations.decorationDash())
            operations.display()

            sellLaptop.sellLaptopMain()

            print(decorations.decorationTilde())
            print(decorations.decorationDash())
                
        elif userChoice == 2:
            exit()
        elif userChoice == 3:
            operations.display()
            input("Press any key to get back to the main screen")  # waiting for user input 
            welcomeScreenMain()  # calls the main screen again
        else:
            exit("\nProgram Closed\n")


welcomeScreenMain()
