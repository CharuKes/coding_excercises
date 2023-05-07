import inflect
p = inflect.engine()
name_input = ''
a = ''
while True:
    try:
        name_input += input("Name:") + " "
        a = name_input.split()
        continue
    except EOFError:
        mylist = p.join(a)
        print(f"Adieu, adieu, to {mylist}")
        break