while True:
    try:
        user_input = input("Enter a string: ").upper()
        a = user_input[:]
        b = len(a)
        if 7 > b > 2:
           if not user_input.isalnum():
                print("Invalid")
                break

           elif user_input.isalpha() or  user_input.isnumeric():
                print("Valid")
                break
           elif user_input[0].isdigit() or user_input[1].isdigit():
               print("Invalid")
               break
           elif user_input[2] == '0':
               print("Invalid")
               break
           elif not user_input[-1].isdigit():
               if any(c.isnumeric() for c in user_input[:-1]):
                   print("Invalid")
                   break
           elif user_input[-1].isdigit():
               if user_input[-2].isdigit():
                   print('Valid')
                   break
               elif (c.isnumeric() for c in user_input[:-3]):
                   print("Invalid")
                   break
           else:
               print("Valid")
               break
        else:
            print("Invalid")
            break
    except ValueError as e:
        print(f"{str(e)}")
        break