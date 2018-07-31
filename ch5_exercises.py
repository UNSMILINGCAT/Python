#!/usr/bin/env python 3.1
def do_plus(num1, num2):
    if (type(num1) == type(1) or type(num1) == type("")
            and type(num2) == type(1) or type(num2) == type("")):
        return num1 + num2
    else:
        raise TypeError("错误的类型 %s 和 %s" % (type(num1), type(num2)))


food_take = {}
food_have = {}


def is_food(food_recipe, icebox):
    """

    :param food_recipe:
    :param food_icebox:
    :return:
    """
    count = 0
    isFood = False
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
        isFood = True
    return isFood


def make_omelet_q3(icebox):
    # if(type(icebox)==type({})):
    def remove_from_fridge(food_recipe):
        # food_take = {}
        # food_have = {}
        # count = 0
        # isFood = False
        # 记录当前菜谱的键
        # for food in food_recipe:
        # for recipe in icebox:
        #     if (food == recipe and icebox[food] >= food_recipe[recipe]):
        #         count = count + 1
        #         food_have[food] = food_recipe[food]
        #         isFood = True
        #         break
        #     elif (food == recipe):
        #         food_have[food] = icebox[food]
        #         isFood = True
        #         break
        # if (isFood != True):
        #     food_have[food] = 0
        # else:
        #     isFood = False
        isfood = is_food(food_recipe, icebox)
        if (isfood):
            print("材料足够")
        else:
            string = "缺少："
            for food in food_have:

                if (food_recipe[food] - food_have[food] == 0):
                    continue
                else:
                    string += " " + food + " " + str(food_recipe[food] - food_have[food]) + " 个"
            # raise LookupError("%s 材料不够，无法完成"% string)
            print("%s 材料不够，无法完成" % string)
            return

        for food in food_recipe:
            if (icebox[food] > food_recipe[food]):
                icebox[food] = icebox[food] - food_recipe[food]
                food_take[food] = food_recipe[food]
            else:
                food_take[food] = icebox.pop(food)
        return food_take

    food_recipe = {"胡萝卜": 1, "土豆": 2, "番茄": 4}
    food_take = remove_from_fridge(food_recipe)
    if (food_take != None):
        print(food_take)


make_omelet_q3({"番茄": 4, "土豆": 6, "胡萝卜": 3})
