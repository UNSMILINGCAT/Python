import ch6_Recipe


class Omelet:
    """

    """

    def __init__(self, kind=None, recipe=ch6_Recipe.Recipe()):
        """
        进行初始化操作，参数为传入一个配方
        :param recipe:
        """
        self.kind = kind
        self.recipe = recipe

    def __ingredients__(self):
        """
        返回配方
        :return :
        """
        return self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        """
        设置kind，根据设置的kind返回配方材料
        :param kind:
        :return:
        """
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients is False:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients

    def set_new_kind(self, name, ingredients):
        """
        设置一个新的配方以及名称
        :param name:
        :param ingredients:
        :return:
        """
        self.kind = name
        self.needed_ingredients = ingredients
        return

    def __known_kinds(self, kind):
        """
        根据传入的kind返回配方材料
        :param kind:
        :return:
        """
        ingredient = self.recipe.get(kind)
        if ingredient is not False:
            return ingredient
        else:
            return False

    def get_ingredients(self, fridge):
        """
        根据配方，从fridge中获取材料。
        :param fridge:
        :return:
        """
        self.from_fridge = fridge.get_ingredients(self)

    # def mix(self):
    #     for ingrdient in self.from_fridge:
    #         print("Mixing %d %s for the %s omelet" % (self.needed_ingredients[ingrdient], ingrdient, self.kind))
    #     self.mixed = True

    def mix(self, isPrint=True):
        """

        :param isPrint:
        :return:
        """
        for ingredient in self.from_fridge:
            if isPrint:
                print("Mixing %d %s for the %s omelet" % (self.from_fridge[ingredient], ingredient, self.kind))
            else:
                break
        self.mixed = True

    def make(self):
        if self.mixed == True:
            print("正在烹饪 %s 蛋卷" % self.kind)
            self.cooked = True

    def quick_cook(self, kind, quantity, fridge):
        """

        :param kind:
        :param quantity:
        :param fridge:
        :return:
        """
