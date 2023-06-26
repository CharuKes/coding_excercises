import math
counter = 0
total = 0
# Create a variable name user_input and ask user to enter a number.
user_input = float(input("please enter a number:"))
# Add while loop where user_input does not equal to -1.
while user_input != -1:
  counter += 1
  total += user_input
  user_input = float(input("please enter a number:"))
# if user input -1 loop will end, it will calculate average of user_inputs excluding -1.
  if user_input == -1:
    print(f"the average of the all the numbers is {total/counter:.2f}")
    
