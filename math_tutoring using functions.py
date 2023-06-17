# Program: This program provides a math tutoring to help younger kids to do
# Author : Avey
# Date: 2/14/2023


"""
            Problem: Create a menu-driven math tutoring program
            Input: random number generator
            Processing: do math calculations based on user selection
            output: calculation result


            Pseudocode;
            1. display the menu
                    a. Addition
                    b. Subtraction
                    c.Multiplication
                    d. Exit the Menu
            2.prompt the user for menu selection
            3. read user input and store it into variable
            4. if menu selection >= 1 and menu selection <= 3
                    a. generate two random numbers between 1-20
                    b. if menu selection == 1
                        result = first random number +second random number
                    c. else if menu sekection ==2,
                        result = first random number - second random number
                    d. else if menu selection == 3,
                        result = first random number * second random number
            5. else if menu selection == 4,
                say goodbye
            6. else if menu selection is anything other than 1-4,
                display invalid selection.

"""
import random

def main():
    menu_selection = 1
    while menu_selection !=4:
        display_menu()
        menu_selection = get_selection()
        process_selection (menu_selection)
        print()
def display_menu():
    print ("Math tutoring Program\n")
    print ("1.Addition")
    print ("2.Subtraction")
    print ("3.Multiplication")
    print ("4.Exit the menu\n")

def get_selection():
    selection = int(input("Enter your selection:"))
    return selection
def process_selection(selection):
    if selection >= 1 and selection <= 3:
        random_num1 = random.randint(1,20)
        random_num2 = random.randint(1,20)
        if selection == 1:
            result = random_num1 + random_num2
            math_operator = "+"
        elif selection == 2:
            result = random_num1 - random_num2
            math_operator = "-"
        elif selection == 3:
            result = random_num1 * random_num2
            math_operator = "*"

    #output
            print (random_num1 , math_operator , random_num2 , "=" , result)
           
    elif selection == 4:
        print("GoodBye")
    else:
        print("Invalid Selection")
        print()

#call the main function
main()
    

'''
selection = 1
while selection !=4:
    #display menu
    print ("Math tutoring Program\n")
    print ("1.Addition")
    print ("2.Subtraction")
    print ("3.Multiplication")
    print ("4.Exit the menu\n")

    #input
    selection = int(input("Enter your selection:"))
    if selection >= 1 and selection <= 3:
        random_num1 = random.randint(1,20)
        random_num2 = random.randint(1,20)
        if selection == 1:
            result = random_num1 + random_num2
            math_operator = "+"
        elif selection == 2:
            result = random_num1 - random_num2
            math_operator = "-"
        elif selection == 3:
            result = random_num1 * random_num2
            math_operator = "*"

    #output
            print (random_num1 , math_operator , random_num2 , "=" , result)
           
    elif selection == 4:
        print("GoodBye")
    else:
        print("Invalid Selection")
        print()

#use break and continue
total = 0
for i in range(20):
    if 1% 2 == 1:
        continue  #if you replace continue with break, it will take you out of the loop, while continue means you are out of current iteration and continues to the next iteration
    total += i
print (total)
'''

    
