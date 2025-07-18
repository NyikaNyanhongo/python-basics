#Display Welcome
print("Welcome to the Restaurant Ordering System!")


#Display Menu Items 
MENU = {
    "burger": 5.99,
    "pizza": 8.49,
    "salad": 4.99,
    "drink": 1.99
}

print("Menu")
for item, price in MENU.items():
        print(f"{item.upper()}: ${price:.2f}")

#Prompt menu selection

  
#Prompt quantity 
#Add to order
#continue odering
#(if no) Calculate total
#Fisplay final summary
#End