def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    if greeting == "hey" or greeting == "hi" or greeting == "how you doing?" or greeting == "how's":
        return 20
    elif greeting == "hello" or greeting == "hello, Newman":
        return 0
    else:
        return 100

if __name__ == "__main__" :
    main()