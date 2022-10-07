list_dishes = []
with open('recipes.txt', 'r', encoding='utf8') as list_of_dishes:

    for line in list_of_dishes:
        dish_name = line.strip()

        dish = {dish_name: []}
        count = list_of_dishes.readline()
        # print(dish)
        for i in range(int(count)):
            ing = list_of_dishes.readline()
            ingredient_name,  quantity, measure = ing.split(' | ')
            food = {"ingredient_name":ingredient_name, "quantity" : int(quantity),"measure" : measure.strip()}
            dish[dish_name].append(food)

        list_of_dishes.readline()
        list_dishes.append(dish)

        # print(dish)
# print(list_dishes)

        # person = int(input('Введите количество персон: '))
def get_shop_list_by_dishes(dishes, person_count):
#     pass
# print(list_dishes)
    for dishes in list_dishes:
        # print(dishes)
        print(dishes.values())
    #     print(dishes.keys())
        # for dish_name,  in dishes:
        # print(list_dishes)
        # print(dishes)
        #     print(dish_name)

        # if dish['dish_name'] == dishes:
        #     print(dish['dish_na


# print(dish_name)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)







