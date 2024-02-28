import os
os.system('cls||clear')

string_fav = input("Enter the name of your favorite restaurant: ")
int_fav = int(input("Enter your favorite number: "))
print(string_fav)
print(int_fav)

int(string_fav)

#Error was thrown because of above statement - ValueError: invalid literal for int() with base 10: 'Rosso'. This is because a string cannot be converetd into an integter


