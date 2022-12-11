cook_book = {}

with open('recipes.txt', 'r', encoding='utf8') as list_of_dishes:
    for line in list_of_dishes:
        dish_name = line.strip()
        cook_book[dish_name] = []
        count = list_of_dishes.readline()
        for i in range(int(count)):
            ing = list_of_dishes.readline()
            ingredient_name, quantity, measure = ing.split(' | ')

            food = {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()}
            cook_book[dish_name].append(food)


        list_of_dishes.readline()
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            cook = cook_book[dish]
            for item in cook:
                if not item["ingredient_name"] in shop_list:
                    shop_list[item["ingredient_name"]] = {"quantity" : 0, "measure" : item["measure"]}
                shop_list[item["ingredient_name"]] ["quantity"] += item["quantity"]*person_count
        else:
            raise Exception("В списке блюд нет блюда f'{dish}'")
    return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет','Утка по-пекински'], 2))






