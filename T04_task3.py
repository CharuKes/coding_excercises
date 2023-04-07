# these are three events of a triathlon, namely swimming, cycling, and running, and user must input the time taken by all the events.
while True:

    try:
        swimming_time = float(input("How many minutes it took you to complete swimming:"))
        if swimming_time < 0 :
            print("Invalid input as Time can not be negative")
            continue

        cycling_time = float(input("How many minutes it took you to complete cycling:"))
        if cycling_time < 0 :
            print("Invalid input as Time can not be negative")
            continue

        running_time = float(input("How many minutes it took you to complete running:"))
        if running_time < 0 :
            print("Invalid input as Time can not be negative")
            continue
        break

    except ValueError:
        print("Invalid input! Please enter valid integer or float")
        
# Create a variable for total time(in minute) taken to complete triathlon : triathlon_time

triathlon_time = swimming_time + cycling_time + running_time

print("Total time taken to complete the triathlon:",triathlon_time,"minute")

# The qualifying time for awards is 100 minutes.(qualifying time=100 minutes)

if triathlon_time <= 100.0:   # if total triathlon time is less than 100 minutes
    print("You have been awarded with Provincial Colours")

elif triathlon_time <= 105.0:   # if total triathlon time is within 5 minute of the qualifying time
    print("You have been awarded with Provincial Half Colours")

elif triathlon_time <= 110.0:   # if total triathlon time is within 10 minute of the qualifying time
    print("You have been awarded with Provincial Scroll")

else:
    print("There is no award")
