# Functions are re-usable pieces of code, anything with parentheses


print()

# we define a function with the word def

def greet(name):
    print(f"Hello,{name}! Welcome to the party!")
    name = name.lower()
    name = name.capitalize()

def user_input(prompt):
    input_value = input(prompt)



def main_menus():
    print("Welcome to the main menu!")
    print("1. Start")
    print("2. Exit")

    choice = input (" Please choose an option: ")
    print (f'You chose option {choice}')
    return choice 

    

    print("Hello!")
    print("My name is Python")
    greet("Mike")


main_menu_choice = main_menu()


if main_menu_choice == 1:
   print ("starting the program...")
else: 
    print("Exiting the program. Goodbye!")