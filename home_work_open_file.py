import os
print(os.getcwd())
file_patch = os.path.join(os.getcwd(), 'recipe.txt')
with open(file_patch, encoding='utf8') as file:
    #print(file.read())
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
cook_book[recepie_name] = ingredients
print(cook_book)

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])
