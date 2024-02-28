import os
os.system('cls||clear')

age = int(input("Enter your age: "))

if age >= 100:
    print("Sorry, you're dead.")
elif 65 <= age < 100:
    print("Enjoy your retirement!")
elif 40 <= age < 65:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")
