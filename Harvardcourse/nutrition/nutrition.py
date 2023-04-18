my_dict = {
           "apple":"Calories: 130","avocado":"Calories:50",
           "sweet cherries":"Calories:100","kiwifruit":"Calories: 90",
           "pear":"Calories: 100"
           }
user_input = input("Item: ").lower()
if user_input in my_dict:
    print(my_dict[user_input], end='')
else:
    print()