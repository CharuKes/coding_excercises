a = input("What is the answer to the Great Question of Life, the Universe and Everything? :").strip(" ")
if a == '42':
    print("Yes")
elif a == 'Forty Two':
    print("Yes")
elif a == 'forty two':
    print("Yes")
elif a == 'FoRty TwO':
    print("Yes")
elif a == 'forty-two':
    print("Yes")
else:
    print("No")