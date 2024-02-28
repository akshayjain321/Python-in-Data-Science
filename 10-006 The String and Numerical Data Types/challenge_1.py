import os
os.system('cls||clear')

import math

#Take input of three sides
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
print("")

#check for valid 3rd length of the triangle
side3 = float(input(f'''The third side must be smaller than the sum of first two slides i.e. {side1+side2}
Enter side 3: '''))

while (side3 >= (side1+side2)):
    side3 = float(input(f'''Your third side needs to be smaller than the sum of first two slides i.e. {side1+side2}
    Enter side 3: '''))


#Calculating area of the triangle
s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(f"The area of the triangle is: {area}")
print("")

