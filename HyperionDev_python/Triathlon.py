''' there are three events of a triathlon, namely swimming, cycling, and running, and user must input the time taken by
all the events, to calculate total time taken to complete triathlon '''

swimming_time = 0      # Created variable name swimming_time to take user's time input to complete swimming
cycling_time = 0       # Created variable name cycling_time to take user's time input to complete cycling
running_time = 0       # Created variable name running_time to take user's time input to complete running

while True:
    try:
        swimming_time = float(input("How many minutes it took you to complete swimming:"))
        if swimming_time > 0:     # If user input is positive integer and float
            print("")
        else:                     # If user input is negative it print error time can not be negative
            print("invalid input!Time can not be negative, try again")
            continue
    except ValueError:            # If user input is non int or non float it print ValueError
        print("Invalid input! Please enter valid integer or float")
        continue
    break

while True:
    try:
        cycling_time = float(input("How many minutes it took you to complete cycling:"))
        if cycling_time > 0:
            print("")
        else:
            print("invalid input!Time can not be negative, try again")
            continue
    except ValueError:
        print("Invalid input! Please enter valid integer or float")
        continue
    break

while True:
    try:
        running_time = float(input("How many minutes it took you to complete running:"))
        if running_time > 0:
            print("")
        else:
            print("invalid input!Time can not be negative, try again")
            continue
    except ValueError:
        print("Invalid input! Please enter valid integer or float")
        continue
    break
# Create a variable for total time(in minute) taken to complete triathlon : triathlon_time
triathlon_time = swimming_time + cycling_time + running_time

print("Total time taken to complete the triathlon:", triathlon_time, "minute")

# The qualifying time for awards is 100 minutes(qualifying time=100 minutes).

if triathlon_time <= 100.0:      # if total triathlon time is less than or equal to 100 minutes print statement below
    print("You have been awarded with Provincial Colours")

elif triathlon_time <= 105.0:    # if total triathlon time is less than or equal to 105 minute print statement below
    print("You have been awarded with Provincial Half Colours")

elif triathlon_time <= 110.0:    # if total triathlon time is less than or equal to 110 minutes print statement below
    print("You have been awarded with Provincial Scroll")

else:      # If total time taken is greater than 110 print statement below
    print("There is no award")
