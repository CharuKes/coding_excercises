def main():
    user_input = input("What's the time?: ").lower().strip('p.m.').strip('a.m.')
    time = convert(user_input)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(':')
    decimal_time = int(hours) + int(minutes) / 60
    return decimal_time

if __name__ == "__main__":
    main()