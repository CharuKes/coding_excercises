user_input = 0
total_input = 0
print("Amount Due: 50")
while True:
    user = int(input("Insert coin:"))
    total_input += user_input
    if user_input == 30:
        print("Amount Due: 50")
        break
    elif user_input <= 50 and user_input != 30:
        a = 50 - total_input
        if total_input >= 50:
            print(f"Change Owed:{total_input-50}")
            break
        print(f"Amount Due:{a}")
    elif user_input >= 50:
        print("Change Owed: 0")