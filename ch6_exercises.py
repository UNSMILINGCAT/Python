class Fridge:
    """
    这是一个类
    """

    def __init__(self, items={}):
        """
        进行一些必要的初始化作用,以及判断传入的类型是否符合，如若不符，则抛出异常
        符合则赋值给成员变量
        :param items:
        """
        if type(items) != type({}):
            raise TypeError("类型错误，接受的类型应是一个dict")
        self.items = items
        return None

    def __add_multi(self, food_name, quantity):
        """
        用于添加的私有方法，供内部使用
        :param food_name:
        :param quantity:
        :return:
        """
        if not food_name in self.items:
            self.items[food_name] = quantity
        else:
            self.items[food_name] += quantity
        return

    def add_one(self, food_name):
        """
        供外部调用的方法，实现单个添加
        :param food_name:
        :return:
        """
        if type(food_name) != type(""):
            raise TypeError("类型错误，只接受一个String，不接受%s类型" % type(food_name))
        else:
            self.__add_multi(food_name, 1)
        return True
    def add_many(self,food_dict):
        """
        供外部使用的添加方法，可以dict导入
        :param food_dict:
        :return:
        """
        if type(food_dict) !=type({}):
            raise TypeError("类型错误，只接受dict类型，不接受%s类型"% type(food_dict))
        else:
            for food in food_dict:
                self.__add_multi(food,food_dict[food])
        return True
    def has(self,food_name,quantity=1):
        """

        :param food_name:
        :param quantity:
        :return:
        """
        if not food_name in self.items :
            return False
        elif(self.items[food_name]<quantity):
            return False
        return True

    def has_various(self,foods):
        """

        :param foods:
        :return:
        """
        try:
            for food in foods:
                if self.has(food,foods[food])!=True:
                    return False
            return True
        except KeyError as error:
            print("Key错误，无此%s Key"% error)
