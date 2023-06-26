''' Created function name options to print out city options for users to select the flight for,
Where 'a' is for Rome, 'b' is for Istanbul, 'c' is for New delhi, 'd' is for Toronto,
If user enters 'q' it will exit the program.'''
def options():
    print("a = Rome.")
    print("b = Istanbul.")
    print("c = New delhi.")
    print("d = Toronto")
    print("q = quit")
    
# Created a dictionary called plane_cost_dict for each flight and its respective cost
plane_cost_dict = {'a': 500, 'b': 490, 'c': 800, 'd': 200}
# Created variable name city_flight to take user's input for flight destination city
city_flight = ""
# Created a function name plane_cost() to return flight cost of respected city present in plane_cost_dict
def plane_cost(city_flight):    
    if city_flight in plane_cost_dict:
        return plane_cost_dict[city_flight]    # Return 'value' of the perticular 'key' in dictionary called plane_cost_dict
    
# Created a dictionary called hotel_cost_dict for each city and respective cost of hotel stay per day
hotel_cost_dict = {'a': 120, 'b': 70, 'c': 50, 'd': 100}
# Created varibale num_nights to take users input for how many days user will stay in the hotel
# Created a function name hotel_cost() to return total cost of hotel stay in respected city present in hotel_cost_dict
def hotel_cost(num_nights, city_flight):
    if city_flight in hotel_cost_dict:
        return hotel_cost_dict[city_flight] * num_nights    #Return 'value' of the perticular 'key' in dictionary called hotel_cost_dict then multiply by num_nights input
    
# Created a dictionary called car_rental_dict for each city and respective cost of renting a car per day
car_rental_dict = {'a': 90, 'b': 100, 'c': 50, 'd': 85}
# Created varibale rental_days to take users input for how many days user will rent a car
# Created a function name car_rental() to return total car rental cost of respected city present in car_rental_dict
def car_rental(rental_days, city_flight):
    if city_flight in car_rental_dict:
        return car_rental_dict[city_flight] * rental_days    #Return 'value' of the perticular 'key' in dictionary called car_rental_dict then multiply by rental_days input
    
# Created a function called holiday_cost to add the other three functions hotel_cost(),plane_cost() and car_rental()
def holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days, city_flight)    # This will add total cost of holiday

# This print statement to show user which city to select along with options funtion below
print(f"Here we have some options for the city you would like to book holiday for:-")
options()

# Created a dictionary called city_dict to represent each option with respective city they represent
city_dict = {'a': 'Rome', 'b': 'Istanbul', 'c': 'New delhi', 'd': 'Toronto'}

# Created while loop to iterate every input entered by user
while city_flight != 'q':     # when city_flight input does not equal to q
    city_flight = input("Which city flight do you want to book?: ")
    
    if city_flight in city_dict:      # If city_flight user's input is in the city_dict
        while True:
            try:
                num_nights = int(input("How many nights do you wanna stay?: "))
                break
            except ValueError:        # If user enters other than number it will show ValueError and ask again
                print("Invalid input!Please try again..")
        while True:
            try:                     
                rental_days = int(input("For how many days whould you like to hire a car?: "))
                break
            except ValueError:       # If user enters other than number it will show ValueError and ask again
                print("Invalid input!Please try again..")

        # this print statement will print total cost of the holiday once user enters all the correct inputs along       
        print(f"Total cost of your holiday including your flights to {city_dict[city_flight]}, hotel stay for {num_nights} days and car rental for {rental_days} days will be ${holiday_cost(num_nights, city_flight, rental_days)}. ")
        break
        
    elif city_flight == 'q':     # If user input 'q' it will exit the program
        print("",)
        
    else:           # If city_flight user's input is not in the city_dict, it will print statement below and ask user again.
        print("Unrecognized option!Please enter one of the option mentioned.")
        options()
