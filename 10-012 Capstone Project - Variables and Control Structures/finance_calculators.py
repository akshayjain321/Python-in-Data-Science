import os
os.system('cls||clear')

import math

################################################################################################################################################### 
# This is program to enable user to access two different financial calculators:
# Investment Calculator and a Home Loan Repayment Calculator
# The user will be asked to choose one of the two calculators
#The code is flexible to how user capitalises their selection. It will display an error message in case of invalid input
###################################################################################################################################################

####### Ask user to select from one of the two calculators #######
selection = input('''1. Investment: To calculate the amount of interest you will earn on your investment
2. Bond: To calculate the amount you will hve to pay on a home loan.
      
Enter with 'investment' or 'bond' from the menue to proceed: ''')
selection = selection.lower() #### Converting user input into lower case to accommodate for any text-capitalisation by the user ####
print("")

####### Check for valid input and ask user to enter again accordingly #######
while (selection!="investment" and selection!="bond"):
    print("Error: Invalid input!")
    selection = input("Enter 'investment' or 'bond': ")
    selection = selection.lower()
   
################################################# Investment Calculator - Begins ###############################################################

#Getting input for investment related details
if selection == "investment":
    deposit = float(input("Enter the deposit amount: "))
    interest_rate = float(input("Enter the interest rate: "))
    years = int(input("Enter the years you plan to invest: "))
    interest = input("Enter if you want 'simple' or 'compound' interest: ")
    interest = interest.lower()
    print("")

    #Checking for valid input for 'simple' or 'compunded' interest, and asking user to input again accordingly
    while (interest!="simple" and interest!="compound"):
        print("Error: Invalid input!")
        interest = input("Enter 'simple' or 'compound': ")
        interest = interest.lower()

    #Calculating & displaying 'simple' interest and total amount after the entered no. of years
    if interest == "simple":
        total_amount = deposit * (1 + ((interest_rate/100) * years))
        print(f"The total interest earned in {years} years is: {total_amount - deposit} \n The total amount after {years} years is: {total_amount}")
        print("")

    #Calculating & displaying 'compound' interest and total amount after the entered no. of years
    if interest == "compound":
        total_amount = deposit * (math.pow((1 + (interest_rate/100)), years))
        print(f"The total interest earned in {years} years is: {total_amount - deposit} \n The total amount after {years} years is: {total_amount}")
        print("")
 
########################################## Investment Calculator - Ends ###############################################################################

########################################## Bond Calculator - Begins ###############################################################################################

#Getting input for investment related details
if selection == "bond":
    house_value = float(input("Enter the value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    monthly_interest_rate = (interest_rate/100)/12
    months = int(input("Enter the months you plan to replay the bond: "))
    print("")

    #Calculating & displaying the monthly repayment
    repayment = (monthly_interest_rate * house_value) / (1 - ((1 + monthly_interest_rate)**(-months)))
    print(f"The monthly repayment amount will be: {math.floor(repayment)}")
    print("")

########################################## Bond Calculator - Ends ###############################################################################################