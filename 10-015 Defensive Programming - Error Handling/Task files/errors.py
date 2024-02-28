# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #Syntax Error: Parentheses were missing for print command
print("\n") #Syntax Error: Indentation error and parantheses were missing

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24"
#runtime error: age_Str not defined
#There should be '=' instead of '==' and "years old" should be removed only "24" should be there

age = int(age_Str)
#SyntaxError: Indentation error

print("I'm " + str(age) + " years old.")
#Syntax Error: Indentation error
#Runtime Error: age is int and therfore should be casted to string again for correct concatenation

# Variables declaring additional years and printing the total years of age

years_from_now = "3"
#SyntaxError: Indentation error

total_years = age + int(years_from_now)
#SyntaxError: Indentation error
#Runtme error: years_from_now needs to be casted into integer to be added to 'age'

print("The total number of years: " + str(total_years))
#SyntaxError: Parentheses were missing
#Logical Error: Instead of answer years it should be total years casted as string

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = total_years * 12
#Runtme error: total not defined, it should be total_years instead

print("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old")
#SyntaxError: Parentheses were missing
#Logical Error: 6 months should be added to total_months to calcuate the right answer
#Runtme error: total_months+6 should be casted as string


#HINT, 330 months is the correct answer

