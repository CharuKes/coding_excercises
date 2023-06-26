import random
user_input = int
while True:
    try:
        user_input = int(input("Level:"))
        if user_input != int:
            if user_input < 0:
                continue
            elif user_input == str:
                continue
            else:
                break
    except ValueError:
        continue
while True:
    try:
        user_input1 = int(input("guess:"))
        if user_input1 < 0:
            continue
        elif user_input1 == str:
            continue
        elif user_input1 == 0:
            continue
        else:
            min_num = min(user_input, user_input1)
            max_num = max(user_input, user_input1)
            r = random.randint(min_num, max_num)
            if r > user_input1:
                print("Too small!")
                continue
            elif r < user_input1:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
    except ValueError:
        continue