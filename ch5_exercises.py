#!/usr/bin/env python 3.1
def do_plus(num1,num2):
    if(type(num1)==type(1) or type(num1)==type("")
       and type(num2)==type(1)or type(num2)==type("")):
        return num1+num2
    else:
        raise TypeError("错误的类型 %s 和 %s"%(type(num1),type(num2)))
    
def make_omelet_q3(icebox):
    if(type(icebox)==type({})):
        def remove_from_fridge(food_recipe):
            food_take={}
            count=0
            for food in icebox:
                for recipe in food_recipe:
                    if(food==recipe and icebox[food]>=food_recipe[recipe]):
                        count=count+1
            else:
                if(count==len(food_recipe)):
                    print("材料足够")
                else:
                    raise LookupError("材料不够，无法完成")
            for food in food_recipe:
                if(icebox[food]>food_recipe[food]):
                    icebox[food]=icebox[food]-food_recipe[food]
                    food_take[food]=food_recipe[food]
                else:
                    food_take[food]=icebox.pop(food)
            return food_take
        food_recipe={"胡萝卜":1,"土豆":2,"番茄":1}
        food_take=remove_from_fridge(food_recipe)
        print(food_take)
