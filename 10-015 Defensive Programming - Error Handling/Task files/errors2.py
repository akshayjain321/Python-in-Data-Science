# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
#Runtime Error: Lion is not defined variable, it should be "Lion" so this value can be assigned to animal

animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
#Logical Error: This entire sentence was being printed as string. f String should be used to insert variable values.
#also 'number of teeth' and 'cub_type' variables should switch respective positions

print(full_spec)
#SyntaxError: Parentheses were missing

