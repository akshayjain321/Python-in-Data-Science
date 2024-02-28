import os
os.system('cls||clear')

# pseudo code
# Take user's name, age, house number and street name
# print all the details in a single line using f-string

name = str(input("Enter the name: "))
age = int(input("Enter the age: "))
house_number = str(input("Enter the house number: "))
street_name = str(input("Enter the street name: "))
print("")
print(f"This is {name}. He is {age} years old and lives at house number {house_number} at {street_name} street.")