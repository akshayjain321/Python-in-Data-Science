import os
os.system('cls||clear')

# ============ Program the total stock worth of cafe menu ============ #

menu = [] # Declare a list called 'menu' to store all menu items
stock = {} # Declare a dictionary called 'stock' to store stock qty for each menu ietm
price = {} # Declare a dictionary called 'price' to store price for each menu item

# ============ Ask user to enter 4 menu items their with individual stock and price ============ #

for i in range (0, 4):
    menu.append (input(f"\nEnter the menu item number {i+1}: "))
    stock[menu[i]] = float(input(f"Enter the stock for {menu[i]} in 'Kgs': "))
    price[menu[i]] = float(input(f"Enter the price for {menu[i]} in '$': "))

# ============ If user wants to add more items to the menu ============ #

i +=1   # Increase the loop counter by 1 if the user wants to add another item
user_choice = "Y"   # Initialise the variable with 'Y' for the loop to run once and take user choice

while (user_choice == "Y"):
    user_choice = input("\nDo you wish to add more items (Y/N): ")
    
    if user_choice == "Y":  # If the user choice is 'Y' then store another menu item, stock and price
        menu.append (input(f"\nEnter the menu item number {i+1}: "))
        stock[menu[i]] = float(input(f"Enter the stock for {menu[i]} in 'Kgs': "))
        price[menu[i]] = float(input(f"Enter the price for {menu[i]} in '$': "))
        i += 1  # Increase the loop counter by 1 if the user wants to add another item

# ============ Calculate the total stock worth ============ #

total_stock_worth = 0 # Declare variable to store total worth of stock

for j in range(len(menu)): #Run the loop for all menu items that were entered
    total_stock_worth = total_stock_worth + (stock[menu[j]] * price[menu[j]]) #Adding stock worth of each item iteratively to total_stock_worth

# Print the menu along with stock and price for each menu item 
print(f"\nThe menu is: {menu}")
print(f"The stock list for menu items in 'Kgs' is: {stock}")
print(f"The price list for menu items in '$' is: {price}")

# Print the calcuated total worth of stock 
print(f"\nThe total stock worth is: ${total_stock_worth} \n"" ")