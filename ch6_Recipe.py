class Recipe:
    """

    """

    def __init__(self):
        self.recipe_names["乳酪"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1}

        self.recipe_names["蘑菇"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "蘑菇": 2}

        self.recipe_names["洋葱"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "洋葱": 1}

    def get(self, recipe_name):
        """
        根据传入的食谱名，获取食谱
        :param recipe_name:
        :return:
        """
        return recipe_name[recipe_name]

    def add(self, recipe_name, ingredients):
        """
        添加新的菜谱进去，如何菜谱为原有的则抛出错误
        :param recipe_name:
        :param ingredients:
        :return:
        """
        if not recipe_name in self.recipe_names:
            self.recipe_names[recipe_name] = ingredients
        else:
            print("菜谱已经存在，无法进行添加")
