import os
os.system('cls||clear')

# This is a program to hanlde strings

# ================= Part 1 ================= #

#Get a string as an input, and convert it into a list of characters
my_string = input("Enter the string: ")
my_string = list(my_string)

#Run a for loop on this list. If the position of the loop counter is even:
#Then replace the character with an uppercase character using string.upper()

for i in range (0,len(my_string)):
    
    if i % 2 == 0:
        my_string[i] = my_string[i].upper()

#Create and print a new string by joining all the characters from the previous list    
new_string = "".join(my_string)
print(new_string)

# ================= Part 2 ================= #
# Take the same string and make alternative words lower and upper case respectively

#Split the string into a list of separate words using split()
final_string = new_string.split()

#Run a for loop on this list. Make alternatives words lower/upper based on loop counter position

for i in range (0,len(final_string)):
    
    if i % 2 == 0:
        final_string[i] = final_string[i].lower()
    else:
        final_string[i] = final_string[i].upper()

#Create and print the final string by joining the above list

final_string = " ".join(final_string)
print(final_string)






