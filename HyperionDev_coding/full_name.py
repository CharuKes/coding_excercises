# Created a variable for full name : full_name
# By using input function ask user for full name and display appropriate message
while True:
    full_name = input("What is your full name?: ")
    # Using len("string") function to return the length of the String
    if len(full_name) == 0:     # If user enters no input
        print("You have not entered anything.Please enter your full name.")     # this message will display
    elif len(full_name) < 4:     # If user enters less than 4 letters
        print("You have entered less than 4 characters.Please make sure that you have entered your name and surname.")
    elif len(full_name) > 25:     # If user enters more than 25 letters
        print("You have entered more than 25 characters.Please make sure that you have only entered your full name.")
    else:
        print("Thank you for entering your name.")    # When user enters right inputs,this message will display
        break
