# Project Title: "Simple Shopping Cart Calculator"
# Project Description:
# You will build a simple shopping cart program that:

# Allows a user to add items to their cart by specifying the item name, price, and quantity.
# Calculates the total cost of the cart.
# Applies discounts based on conditions (e.g., if the total cost exceeds $100).
# Compares the final total to a user's budget to determine if they can afford it.
# Requirements:
# 1. Use Data Types:
# Strings for item names.
# Floats/integers for prices and quantities.
# Boolean values for applying discounts or checking the budget.
# 2. Incorporate Operators:
# Arithmetic: Add prices, multiply price and quantity, apply discounts.
# Comparison: Compare total to discount thresholds or user budget.
# Logical: Combine conditions (e.g., apply discounts only if the total exceeds a certain amount and the cart is not empty).
# Steps to Implement:
# Input Details for Items:

# Prompt the user to input an item name, price, and quantity.
# Store this information in a dictionary or list.
# Calculate Total Cost:

# Multiply the price of each item by its quantity.
# Add the cost of all items to get the total cost.
# Apply Discounts:

# If the total exceeds $100, apply a 10% discount.
# If the total is less than $50, add a $5 delivery charge.
# Check Budget:

# Ask the user for their budget.
# Compare the final total to their budget and inform them if they can afford it.
# Display the Results:

# Print out the list of items, the subtotal, any discounts or fees, and the final total.
# Indicate whether the user is within budget.
# Bonus Features:
# Add a "Remove Item" option to update the cart dynamically.
# Validate user input to ensure prices and quantities are numbers.
# Format the total cost to two decimal places for currency.

shoppingItems = {
    "Item0": {"name": "Apple", "price": 1.5},
    "Item1": {"name": "Banana", "price": 0.5},
    "Item2": {"name": "Orange", "price": 0.75},
    "Item3": {"name": "Milk", "price": 3.0},
    "Item4": {"name": "Bread", "price": 2.5},
    "Item5": {"name": "Eggs", "price": 5.0}
}

userCart = []

def shoppingCartProgram():
    totalCost = sum(item["price"] * item["quantity"] for item in userCart)
    
    if totalCost > 100:
        totalCost -= totalCost * 0.10
    elif totalCost < 50:
        totalCost += 5.00
    
    print("Items in your cart:")
    for item in userCart:
        print(f"{item['quantity']} x {item['name']} at ${item['price']:.2f} each")

    print(f"Subtotal: ${totalCost:.2f}")
    budget = float(input("What is your budget? "))
    if totalCost > budget:
        print("You cannot afford this. Please remove some items.")
    else:
        print("You are within budget. Thank you for shopping!")

print("Welcome to Dominic's Grocery Store!")
print("Here are some things we offer:")
for key, item in shoppingItems.items():
    print(f"{key[-1]}: {item['name']} - ${item['price']:.2f}")

while True:
    askingTheUser = int(input("\nWhat would you like to see (0-5 numbers only, -1 to finish)? "))
    if askingTheUser == -1:
        break
    elif 0 <= askingTheUser <= 5:
        item = shoppingItems[f"Item{askingTheUser}"]
        print(f"{item['name']} added to cart")
        quantity = int(input(f"How many {item['name']} would you like? "))
        userCart.append({"name": item["name"], "price": item["price"], "quantity": quantity})
    else:
        print("Invalid selection. Please choose a number between 0 and 5.")

shoppingCartProgram()
