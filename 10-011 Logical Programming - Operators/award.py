import os
os.system('cls||clear')

swim_time = float(input("Enter the swimming time in minutes: "))
cycle_time = float(input("Enter the cycling time in minutes: "))
run_time = float(input("Enter the running time in minutes: "))

total_time = swim_time + cycle_time + run_time
print(f"Your total time for Triathlon was: {total_time} minutes")
print("")


if 0 < total_time < 101:
    print("Your award is Provincial Colours")
elif 101 <= total_time < 106:
    print("Your award is Provincial Half Colours")
elif 106 <= total_time < 111:
    print("Your award is Provincial Scroll")
else:
    print("There is no award for you")

print("")

