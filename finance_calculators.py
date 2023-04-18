import math

# Created variable name user_input to show user the choices and ask user for input that they want to be calculated
while True:    # Using while loop to loop over user_input, if user_input is not correct
    user_input = input('\n'"Please select an option" "\n" "\n"
                       "investment - to calculate the amount of interest you'll earn on your investment" "\n"
                       "bond - to calculate the amount you'll have to pay on a home loan" "\n" "\n"

                       "Enter either 'investment' or 'bond' from the menu above to proceed:")

    # create variable name user_investment for 'investment' and user_bond for 'bond'
    user_investment = "investment"
    user_bond = "bond"

# If user input 'investment',lower or capital letter or any other it will accept the input
    if user_input.lower() == "investment":    # Using if statement to iterate over user_input
        # Created some more variable below named r, P, t, A, d
        ''''r' is the interest entered above divided by 100, e.g. if 8% is entered,then r is 0.08.
           'P' is the amount that the user deposits.
           't' is the number of years that the money is being invested.
           'A' is the total amount once the interest has been applied.
           'd' is yearly interest rate'''
        while True:
            try:
                P = float(input("Please enter the amount of deposit: "))
                if P < 0:     # If p's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input! Please enter positive integer or float.")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break
        while True:
            try:
                d = float(input("Yearly rate of interest: "))
                if d < 0:  # If d's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input! Please enter positive integer or float.")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break

        while True:
            try:
                t = float(input("Number of years plan to invest: "))
                if t < 0:  # If t's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input! Please enter positive integer or float.")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break
        r = float(d / 100)    # Function to calculate rate of interest percentage yearly
        while True:
            try:
                interest_type = input("What interest do you want (simple/compound): ")
                # If user input interest_type simple
                if interest_type == "simple":
                    A = P * (1 + r * t)  # Function to calculate simple interest
                    # Final print statement for investment after calculating at simple interest
                    print(f"The investment amount will be {A:.2f} after {t} years, at simple interest ")
                    break
                # If user input interest_type compound
                elif interest_type == "compound":
                    B = P * math.pow((1 + r), t)  # Function to calculate compound interest
                    # Final print statement for investment after calculating at compound interest
                    print(f"The investment amount will be {B:.2f} after {t} years, at compound interest ")
                    break
                else:
                    print("invalid input! Enter simple or compound")
                    continue
            except ValueError:
                print("invalid input! Enter simple or compound")
                continue
        break
    # If user input bond
    elif user_input.lower() == "bond":
        ''' Created some more variable below named Q, k, i, n
          'Q' is the present value of the house
          'k' is yearly interest rate
          'i' is monthly interest /100
          'n' is number of months plan to invest'''
        while True:
            try:
                Q = float(input("The present value of the house: "))
                if Q < 0:    # If Q's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input!please enter positive value")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break
        while True:
            try:
                k = float(input("The yearly interest rate: "))
                if k < 0:    # If k's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input!please enter positive value")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break
        while True:
            try:
                n = float(input("Number of months plan to invest: "))
                if n < 0:    # If n's input is other than positive int ot float, it will ask user to re-enter the input
                    print("Invalid input!please enter positive value")
                    continue
            except ValueError:
                print("Invalid input! Please enter positive integer or float.")
                continue
            break
        i = (k / 100) / 12    # Function to calculate rate of interest percentage monthly
        repayment = (i * Q) / (1 - (1 + i) ** (-n))  # Function to calculate bond repayment
        # Final print statement for bond repayment after calculation
        print(f"The monthly bond repayment amount  = {repayment:.2f} ")

    else:
        print('\n'"Invalid Input!Please enter 'investment' or 'bond' . ")
        continue
    break
