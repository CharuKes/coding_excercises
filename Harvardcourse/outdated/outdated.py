my_dict = {
    "January": '01',
    "February": '02',
    "March" : '03',
    "April" : '04',
    "May" : '05',
    "June" : '06',
    "July" : '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
}
my_dict1 = {'1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09', '10': '10', '11': '11', '12': '12'}

while True:
    a = input("Date:")
    b = a.replace(',', '')
    b = b.split()
    c = a.replace("/", " ").split()

    try:
        if len(b) == 3 and b[1].isdigit() and b[2].isdigit():
            if ',' not in a:
                continue
            else:
                b.reverse()
                input1 = b.pop(0)
                input2 = b.pop(1)
                input3 = b.pop()
                if int(input3) > 31:
                    continue
                else:
                    for i in my_dict:     # 1636-09-08
                        if i in input2:
                            my_dict[input2]
                    for j in my_dict1:
                        if j in input3:
                            my_dict1[input3]
                    d = [ input1 , my_dict[input2], my_dict1[input3]]
                    print("-".join(d))
                    break
        elif len(c) == 3 and c[0].isdigit() and c[1].isdigit():
            c.reverse()
            input1 = c.pop(0)
            input2 = c.pop(1)
            input3 = c.pop()
            if int(input2) > 12 or int(input3) > 31:
                continue
            else:
                for i in my_dict1:
                    if i in input2:
                        continue
                    if i in input3:
                        continue
                d = [input1, my_dict1[input2], my_dict1[input3]]
                print("-".join(d))
                break
        else:
            continue
    except ValueError:
        raise ValueError
        break