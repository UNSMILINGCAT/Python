class Omelet:
    """

    """

    def __init__(self, kind=None):
        """

        :param str kind:
        """
        self.set_kind(kind)
        return

    def __ingredients__(self):
        """

        :return:
        """
        return self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients

    def set_new_kind(self, name, ingredients):
        self.kind = name
        self.needed_ingredients = ingredients
        return

    def __known_kinds(self, kind):
        if kind == "乳酪":
            return {"鸡蛋": 2, "牛奶": 1, "乳酪": 1}
        elif kind == "蘑菇":
            return {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "蘑菇": 2}
        elif kind == "洋葱":
            return {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "洋葱": 1}
        else:
            return False

    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self)

    def mix(self, isPrint=True):
        for ingrdient in self.from_fridge:
            if isPrint:
                print("Mixing %d %s for the %s omelet" % (self.from_fridge[ingrdient], ingrdient, self.kind))
        self.mixed = True

    def make(self):
        if self.mixed == True:
            print("正在烹饪 %s 蛋卷" % self.kind)
            self.cooked = True
