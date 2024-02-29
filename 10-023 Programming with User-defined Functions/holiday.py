import os
os.system('cls||clear')

# This is a program to caulculate total holiday costs

# Function to calculcate the Hotel costs
def hotel_cost(nights):
    while (True):    # Loop runs until valid input from user
        room_type = (input(f'''
Which room type would you prefer: 
    1. Double: ${room_costs['double']} per night    
    2. Premimum: ${room_costs['premium']} per night
Please enter the room type: '''))                   
        if room_type.lower() == "double":
            # Retrieves room rate from room_costs dictionary
            # calculate and returns hotel costs & breaks away from loop
            return nights * room_costs["double"]
        elif room_type.lower() == "premium":
            return nights * room_costs["premium"]
        else:
            print("\nInvalid input, plese enter again")

# Function to calculcate the flight costs
def plane_cost(destination):
    # Retrieves flight cost from the city_flight_costs dictionary
    flight_cost = city_flight_costs[destination]
    return flight_cost

# Function to calculcate the ar rentak costs
def car_rental(car_days):
    while (True):   # Loop will run until the user provides valid input
        room_type = (input(f'''
Which car type would you prefer: 
    1. Sedan: ${car_rental_costs['Sedan']} per day
    2. SUV: ${car_rental_costs['SUV']} per day
Please enter the car type: '''))
        # Retrieves car rate from car_rental_costs dictionary
        # calculate and returns car rental costs & breaks away from loop
        if room_type.lower() == "sedan":
            return car_days * car_rental_costs['Sedan']    
        elif room_type.lower() == "suv":
            return car_days * car_rental_costs['SUV']
        else:
            print("\nInvalid input, plese enter again")

# Function to calculcate total holiday costs
def holiday_costs(flight_cost, hotel_cost, car_cost):
    return flight_cost + hotel_cost + car_cost

# Function to calculcate total holiday costs
def city_options():
    while (True):    # Loop will run until the user provides valid input
        print("\n1. London")
        print("2. Paris")
        print("3. New York")
        print("4. Melbourne")
        user_choice = input("\nEnter name of the city from the list: ")
        if ((user_choice.lower() == "london") or 
            (user_choice.lower() == "paris") or 
            (user_choice.lower() == "new york") or 
            (user_choice.lower() == "melbourne")):
            return user_choice.lower()
        else:
            print("\nInvalid input, plese enter again")
            

# Define dictionaries for flight, hotel room, car rental prices
# Created dictionaries because options can be added/edited over time
city_flight_costs = ({'london': 300, 'paris': 450, 'new York': 150, 
                      'melbourne': 500})
room_costs = {'double': 150, 'premium': 200}
car_rental_costs = {'Sedan': 100, 'SUV': 200}

# Calculate the flight costs
print("\nWhich city would you like to travel? ")
city_flight = city_options()
cost_of_flight = plane_cost(city_flight)

# Calculate the hotel costs
num_nights = int(input("\nPlease enter the number of nights for your " 
                       "hotel stay: "))
cost_of_hotel = hotel_cost(num_nights)

# Calculate the car rental costs
rental_days = int(input("\nPlease enter the number of days for your "
                        "car rental: "))
cost_of_car = car_rental(rental_days)

# Calculate the total holiday costs
total_holiday_cost = (holiday_costs(cost_of_flight, cost_of_hotel,
                                    cost_of_car))

# Print the calculations
print("\n*****************************************")
print(f"\nYour Flight cost is: ${cost_of_flight}")
print(f"\nYour Hotel cost is: ${cost_of_hotel}")
print(f"\nYour Car Rental cost is: ${cost_of_car}")
print(f"\nYour Total holiday cost is: ${total_holiday_cost}\n")
print("*****************************************\n")



        




 
