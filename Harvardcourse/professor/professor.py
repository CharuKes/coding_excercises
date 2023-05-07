import random

def main():
    level = get_level()
    score = play_game(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            user_input = int(input("level: "))
            if user_input not in [1, 2, 3]:
                continue
            else:
                return user_input
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

def play_game(level):
    num_correct = 0
    for i in range(10):
        a, b = generate_integer(level)
        c = a + b
        total = int(input(f"{a} + {b} = "))
        if c != total:
            for j in range(2):
                print("EEE")
                total = int(input(f"{a} + {b} = "))
                if c == total:
                    break
            else:
                print(f"Correct answer: {a} + {b} = {c}")
        else:
            print("Correct!")
            num_correct += 1
    return num_correct

if __name__ == "__main__":
    main()
