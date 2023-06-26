counts = {}
while True:
    try:
        user_input = input("").upper()
        if not user_input:
            raise KeyError("Error")
            continue
        elif user_input in counts:
            counts[user_input] += 1
            continue
        else:
            counts[user_input] = 1
    except EOFError:
        for string, count in sorted(counts.items()):
            if count >= 1:
                print(f"{count} {string}")
        break