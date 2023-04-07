flag = True
while flag:
# Create a variable for full name : full_name 
# Ask user for full name by using input function and display appropriate message
    full_name = input("What is your full name?: ")
#A useful function is len("string") function which returns the length of the String
#Using if statements becuase it contains condition
    if len(full_name) == 0: #If user enters no input 
        print("You have not entered anything.Please enter your full name.") #this message will display
    elif len(full_name) < 4 : #If user enters less than 4 inputs
        print("You have entered less than 4 characters.Please make sure that you have entered your name and surname.") #this message will display
    elif len(full_name) > 25 : #If user enters more than 25 inputs
        print("You have entered more than 25 characters.Please make sure that you have only entered your full name.") #this message will display
    else:
        print("Thank you for entering your name.") #When user enters right inputs,this message will display
        flag = False  

    

