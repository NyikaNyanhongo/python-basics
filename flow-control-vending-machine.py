# Vending Machine Simulator

# Step 1: Set up the product menu
items = {
    "soda": 1.50,
    "chips": 2.00,
    "candy": 1.00,
    "caviar": 12.00,
    "brisket": 8.50,
    "burnt-ends": 7.25
}

# Step 2: Prompt for initial funds
funds = float(input("Please input the amount of money you have: "))
print(f"You entered: ${funds:.2f}")

#This is the  Optional part of exercise: Track purchases and total spent
purchased_items = []
total_spent = 0.0

# Step 3: Display the menu
print("\nAvailable items:")
for item, price in items.items():
    print(f"- {item.title()}: ${price:.2f}")

# Step 4: Start transaction loop
while funds > 0:
    print(f"\nYour current balance: ${funds:.2f}")
    choice = input("Select an item (or type 'exit' to quit): ").lower()

    if choice == "exit":
        break

    if choice not in items:
        print("Item not found. Please select a valid item from the menu.")
        continue

    price = items[choice]

    if funds >= price:
        funds -= price
        purchased_items.append(choice)
        total_spent += price
        print(f"Dispensing {choice}. Remaining balance: ${funds:.2f}")
    else:
        print(f"Insufficient funds for {choice}. It costs ${price:.2f}.")
        add_more = input("Would you like to add more money? (yes/no): ").lower()
        if add_more == "yes":
            extra = float(input("Enter additional amount: "))
            funds += extra
        else:
            print("Transaction cancelled.")
            break

    another = input("Would you like to buy another item? (yes/no): ").lower()
    if another != "yes":
        break

# Step 5: Final summary section: 
print("\nThank you for using the vending machine!")
print(f"Remaining balance: ${funds:.2f}")

# Here we Show purchase summary
if purchased_items:
    print("\nPurchase summary:")
    for item in purchased_items:
        print(f"- {item.title()}")
    print(f"Total spent: ${total_spent:.2f}")