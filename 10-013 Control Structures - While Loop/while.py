import os
os.system('cls||clear')

import math

#========= Keep taking a number as input from user until they enter -1 ==============#
#========= if they enter -1, display the average of the numbers =====================#

num = 0
sum = 0
count = 0

while (num != -1):
    num = int(input("Enter a number: "))
    if num!= -1:
        count +=1
        sum = sum + num
    if num == -1:
        if count == 0:
            print("Your first entered number was -1, so the average of numbers cannot be calculated")
        else:
            print(f"The average of the numbers is: {sum/count}")
            print("")

