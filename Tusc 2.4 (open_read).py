with open('recipes.txt') as f:
    ingredients = []
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        #print(dish_name)
        number_of_entries = f.readline()
        ingredients = []
        for ingredient in range(int(number_of_entries)):
            ingredients_dict = {}
            ingredient = f.readline().strip().split('|')
            ingredient_name, quantity, measure = ingredient
            ingredients_dict['ingredient_name'] = ingredient_name
            ingredients_dict['quantity'] = quantity
            ingredients_dict['measure'] = measure
            ingredients.append(ingredients_dict)
        cook_book[dish_name] = ingredients
        f.readline()
    print(cook_book)
    print()

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for dish in dishes:
        for (key, value) in cook_book.items():
            if dish == key:
                for entry in value:
                    a = (entry['ingredient_name']).strip()
                    b = (entry['measure']).strip()
                    c = int((entry['quantity']).strip())
                    if a in result_dict.keys():
                        result_dict[a]['quantity'] = c * person_count + (result_dict[a]['quantity'])
                    else:
                        result_dict[a] = {'measure': b, 'quantity': c * person_count}
    print(result_dict)

get_shop_list_by_dishes(['Омлет', 'Запеченый картофель', 'Фахитос'], 2)