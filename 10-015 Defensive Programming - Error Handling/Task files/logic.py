#This is a program to display a logical error

#Calculate and print semi-perimeter of a triangle

side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))
#Logical error: Additional logic should be inserted to check if the third side is greater than sum of first two sides.
#If not, then user should be asked to enter a valid side 3 again.

semi_perimeter = side_1 + side_2 + side_3 / 2
#Logical error: correct formula should be (side_1 + side_2 + side_3)/2

print(semi_perimeter)