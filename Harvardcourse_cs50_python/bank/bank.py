user_input = input("Greeting: ").strip(" ")
match user_input:
    case "Hey"|"Hi"|"How you doing?"|"How's":
        print("$20")
    case "Hello"|"Hello, Newman":
        print("$0")
    case _:
        print("$100")