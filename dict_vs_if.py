food_item = input('Enter food item name: ')


# def get_price():
#     if food_item == 'mango':
#         return 10
#     elif food_item == 'apple':
#         return 5
#     else:
#         return 0

# price = get_price()


def get_price2():
    return food_items_dict.get(food_item, 0)


food_items_dict = {
    'mango': 10,
    'apple': 5
}


price = get_price2()

print(f'Price of {food_item} is {price}')
