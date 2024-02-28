import os
os.system('cls||clear')

#Take a string as input and print its length
str_manip = input("Enter a string: ")
print("")
print(f"The length of the string is: {len(str_manip)}")
print("")


#Replace last letter with @
last_letter = str_manip[-1]
new_string = str_manip.replace(last_letter, "@")
print(f"The new string with last letter replaced by @ is: {new_string}")
print("")

#Print last 3 characters backwards
print(f"The last three letters are: {str_manip[:-4:-1]}")
print("")

#Create 5 letter word with first 3 and last 2 characters in the string
first_three_letters = str_manip[0:3]
last_two_letters = str_manip[-2:]
new_word = first_three_letters+last_two_letters
print(f"The new 5 letter words is: {new_word}")
print("")