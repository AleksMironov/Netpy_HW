recipes = []

with open('recepies.txt', 'rt', encoding='utf8' ) as file:
    for text in file:
        dish_name = text.strip()
        dish = {"name": dish_name, "ingredients": []}
        ingredients_count = file.readline()
        for ing in range(int(ingredients_count)):
            ingredients = file.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        recipes.append(dish)

def get_shop_list_by_dishes(list_dish, people):
    result = {}
    for dish in list_dish:
        for dish_book in recipes:
            if dish_book['name'] == dish:
                for ing in dish_book['ingredients']:
                    if ing['name'] not in result.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity'])
                        result[ing['name']] = {'measure': measure, 'quantity': quantity}
                    
                    elif ing['name'] in result.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity']) + int((result[ing['name']])['quantity'])
                        result[ing['name']] = {'measure': measure, 'quantity': quantity}
    return result

print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 4))