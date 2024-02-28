import os
os.system('cls||clear')

# This is a program to print a specified pattern using single for-loop, and if-else statement
# I have used two approches to achieve this
# 1st approach is to simply print the specified pattern in the task
# 2nd approach is to take 'range' of stars as input from user, and then print the pattern

# ============ First Approach ============ #

stars = "*****"

for i in range (1, 10):
    if i <= 5:
        print(stars[0:i])
    else:
        print(stars[0:(10-i)])


# ============ Second Approach ============ #

print("\n 2nd Approach: ")
num_range = int(input("Enter range of stars for the pattern: "))
stars = "*" * num_range

for i in range (1, (num_range*2)):
    if i <= num_range:
        print(stars[0:i])
    else:
        print(stars[0:((num_range*2)-i)])


        

