#!/usr/bin/env python 3.1
def do_plus(num1, num2):
    if (type(num1) == type(1) or type(num1) == type("")
            and type(num2) == type(1) or type(num2) == type("")):
        return num1 + num2
    else:
        raise TypeError("错误的类型 %s 和 %s" % (type(num1), type(num2)))


food_have = {}


def is_food(food_recipe, icebox):
    """

    :param food_recipe:
    :param dict icebox:
    :return:
    """
    count = 0
    have_food = False
    for food in food_recipe:
        if not food in icebox:
            food_have[food] = 0
            break
        elif food_recipe[food] > icebox[food]:
            food_have[food] = icebox[food]
            print(food_have)
        else:
            food_have[food] = food_recipe[food]
            print(food_have)
            count += 1
    if count == len(food_recipe):
        have_food = True
    return have_food


def make_omelet_q3(icebox):
    def remove_from_fridge(food_recipes):
        food_takes = {}
        have_food = is_food(food_recipes, icebox)
        if have_food:
            print("材料足够")
        else:
            string = "缺少："
            for food in food_have:

                if food_recipes[food] - food_have[food] == 0:
                    continue
                else:
                    string += " " + food + " " + str(food_recipes[food] - food_have[food]) + " 个"
            # raise LookupError("%s 材料不够，无法完成"% string)
            print("%s 材料不够，无法完成" % string)
            return
        for food in food_recipes:
            if icebox[food] > food_recipes[food]:
                icebox[food] = icebox[food] - food_recipes[food]
                food_takes[food] = food_recipes[food]
            else:
                food_takes[food] = icebox.pop(food)
        return food_takes

    food_recipe = {"胡萝卜": 1, "土豆": 2, "番茄": 4}
    food_take = remove_from_fridge(food_recipe)
    if food_take is not None:
        print(food_take)


make_omelet_q3({"番茄": 4, "土豆": 6, "胡萝卜": 3})
