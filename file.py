list_dishes = []
dishes_1 = []
with open('recipes.txt', 'r', encoding='utf8') as list_of_dishes:
    for line in list_of_dishes:
        dish_name = line.strip()
        # dishes_1.append(dish_name)
        dish = {dish_name: []}
        count = list_of_dishes.readline()
        for i in range(int(count)):
            ing = list_of_dishes.readline()
            ingredient_name, quantity, measure = ing.split(' | ')

            food = {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()}
            dish[dish_name].append(food)
            # print(food)

        list_of_dishes.readline()
        list_dishes.append(dish)
        print(dish)




# print(*list_dishes)
# from function import get_shop_list_by_dishes

# get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 2)




