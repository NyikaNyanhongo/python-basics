# display a menu of items with prices

items = {"Soda": 1.50 ,
         "Chips": 2.00 ,
         "Candy": 1.00 ,
         "Water": 1.25}



#prompt user to insert money 30
funds = float(input("Please input the amount of Money you have: "))


#Display the menu

for item , price in items.items():
    print(f"-{item}: ${price:.2f}")

    
#Allow user to select an item
#Check if user has enough funds to purchase selected item
#Dispenses the item(displays sucess message) and subtracts the cost from the user's funds
#Offers the user the opportunity to make additional purchases or exit the simulation 