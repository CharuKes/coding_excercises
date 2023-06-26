while True:
    # Created variable name user_input to take users input
    # Created short input '1' for 'two numbers and an operator' and '2' for 'to read file' .
    user_input = input("For simple calculator application enter '1',\n"
                       "To read all of the equations from a txt file enter '2': ")
    if user_input == "1":
        while True:
            try:
                num1 = float(input("Please enter first number: "))    # Created variable name 'num1' for first number
                break
            except ValueError:
                # If user enters other than numbers it will give error
                print("Invalid number! That was not a valid number. Try again: ")
        while True:
            try:
                num2 = float(input("Please enter second number:"))  # Created variable name 'num2' for second number
                break
            except ValueError:
                print("Invalid number! That was not a valid number. Try again: ")
        while True:
            try:
                # Created variable name input_operation to take user inputs of operator
                input_operation = input("Please enter operation (e.g. +, -, *, **, / .): ")
                # If user enters any of these operator presented in the list it will perform calculation
                if input_operation in ['+', '-', '*', '/', '**']:
                    result = eval(f"{num1} {input_operation} {num2}")
                    print("\nyour equation is {} {} {} = {}.\n".format(num1, input_operation, num2, result))
                    equation_file = open("equation.txt", 'a')
                    equation_file.write(f"\n{num1} {input_operation} {num2} = {result:.2f}")
                else:       # else user gets ValueError
                    raise ValueError("Invalid operator entered!")
                break
            except ValueError:
                print("Invalid operator! That was not a valid operator. Try again: ")
            except ZeroDivisionError:     # throw zero division error if user tries to divide number by '0'
                print("Sorry! You cannot divide by zero. Try again: ")
    elif user_input == "2":
        while True:
            try:
                file_name = input("Please enter the filename:")   # Create variable file_name to take filename from user
                equation_file = open("equation.txt", 'a')
                if file_name == "equation.txt":    # If user enter the file name 'equation.txt'
                    equation_file = open("equation.txt", 'r')    # this will read the file equation_file
                    print(equation_file.read(), "\n")    # it will print all the equations in the file to the users
                    break
                else:
                    # Raise file not found error if user enters wrong file name
                    raise FileNotFoundError("Oops! File not found enter correct file name: ")
            except FileNotFoundError:
                print("File not found! Please enter correct file name: ")
    else:
        print("Invalid input! Please enter valid input")     # If user enters other than '1' or '2
