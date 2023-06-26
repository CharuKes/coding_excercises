total = 0
my_dict = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
}
while True:
    try:
        user_input = input("Item:").title()
        if user_input in my_dict:
            total += my_dict[user_input]
            print(f"${total:.2f}")
        elif user_input == '':
            break
        else:
            continue
    except EOFError:
        break
