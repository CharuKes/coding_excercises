menu_list = ['item1', 'item2', 'item3', 'item4']     # Created list called menu_list for all the items in the menu
# Created a dictionary name stock_dict for haw many stock is in there for each item
stock_dict = {'item1': 3, 'item2': 4, 'item3': 8, 'item4': 5}
# Created a dictionary name price_dict to know what is the price of each item
price_dict = {'item1': 12, 'item2': 22, 'item3': 24, 'item4': 45}
total_value = 0     # Initialize a variable to keep track of the total stock worth
'''Using for loop to loop through the menu list, the items is set as keys to access the corresponding stock and 
price values. Each item_value is calculated by multiplying stock value by the price value'''
for item in menu_list:
    item_value = (stock_dict[item] * price_dict[item])
    total_value += item_value     # Add the item's value to the total stock worth
# Printing total item value at cafe
print(f"Total stock worth in the cafe : ${total_value}")
