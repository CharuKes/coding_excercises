empty_string1 = ""        # Created variable name empty_string for empty string
my_string = input("PLease enter your sentence here: ")   # Created variable name my_string to get input from user
split_str = my_string.split()    # Created variable name split_str to split input from user in variable my_string
empty_string2 = []      # Created variable name empty_string2 for empty string

for i in range(len(my_string)):         # Using for loop with range for iteration in my_string
    if i % 2 == 0:                      # If 'i' is ie: index divided by is '0' then convert my_string into upper case 
        empty_string1 += my_string[i].upper()
    else:                               # Else lower care
        empty_string1 += my_string[i].lower()
print(f"Your alternate character string : {empty_string1}")

for j in range(len(split_str)):         # Using for loop with range for iteration in split_str
    if j % 2 == 1:                      # If 'j' leaves remainder '1' when divided by '2, convert word to upper else lower
        empty_string2.append(split_str[j].upper())
    else:
        empty_string2.append(split_str[j].lower())
print(f"Your alternate word string: {' '.join(empty_string2)}")    # Using join function to join the strings


