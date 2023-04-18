my_string = input("PLease enter your sentence here: ")
new_string = ''

for i in my_string:
    if i == i.upper():
        new_string += ' ' + i
    else:
        new_string += i + ""

new_string1 = new_string.lower().replace(" ", "_")
print(new_string1)
