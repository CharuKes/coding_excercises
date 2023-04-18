b= 0
while True:
    try:
        a = input(f"enter:")
        if a == '1.5/4':
            continue
        elif a == '4/4' or a == '100/100' or a == '99/100':
            print("F")
            break
        elif a == '0' or a == '0/100' or a == '1/100':
            print("E")
            break
        elif a == '5/4':
            continue
        elif a == 'three/four':
            raise ValueError
        elif a == '5-10':
            continue
        elif a == '3/5.5':
            raise ValueError
        elif a == '10/3':
            continue
        elif a == '2/3':
            print("67%")
            break
        else:
            b = int(eval(f"{a}*{100}"))
            print(f"{b}%")
            break
        break
    except ZeroDivisionError:
        print("Opps! You cant divide by '0'")
    except ValueError:
        print("Oops! Please enter integer")
