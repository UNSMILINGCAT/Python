class Fridge:
    """
    这是一个类
    """

    def __init__(self, items=None):
        """
        进行一些必要的初始化作用,以及判断传入的类型是否符合，如若不符，则抛出异常
        符合则赋值给成员变量
        :param dict items:
        """
        if items is None:
            items = {}
        if type(items) != type({}):
            raise TypeError("类型错误，接受的类型应是一个dict")
        self.items = items

    def __add_multi(self, food_name, quantity):
        """
        用于添加的私有方法，供内部使用
        :param str food_name:
        :param int quantity:
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
        如何添加成功则返回一个True
        :param str food_name:
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
        成功则返回True
        :param dict food_dict:
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
        判断冰箱的食物是否符合要求
        成功则返回True否则返回False
        :param str food_name:
        :param int quantity:
        :return:
        """
        if not food_name in self.items :
            return False
        elif(self.items[food_name]<quantity):
            return False
        return True

    def has_various(self,foods):
        """
        通过传递进来的dict进行判断是否符合要求，
        全部通过返回True
        反之则False
        :param dict foods:
        :return:
        """
        try:
            for food in foods:
                if self.has(food,foods[food])!=True:
                    return False
            return True
        except KeyError as error:
            print("Key错误，无此%s Key"% error)

    def __get_multi(self,food_name,quantity=1):
        """
        内部方法，提供查询作用，
        成功返回查找的数量
        反之为False
        :param str food_name:
        :param int quantity:
        :return:
        """
        try:
            if(self.items[food_name] is None):
                return False
            if(quantity>self.items[food_name]):
                return False
            if self.items[food_name]==quantity:
                self.items.pop(food_name)
            else:
                self.items[food_name]-=quantity;
        except KeyError:
            return False
        return quantity

    def get_one(self,food_name):
        """

        :param str food_name:
        :return:
        """
        if type(food_name)!=type(""):
            raise TypeError ("类型不匹配，应该String 而不是%s"% type(food_name))
        else:
            result=self.__get_multi(food_name,1)
            return result
    def get_many(self,food_dict):
        """

        :param dict food_dict:
        :return dict:
        """
        if self.has_various(food_dict):
            foods_remove={}
            for item in food_dict:
                foods_remove[item]=self.__get_multi(item,food_dict[item])
            return foods_remove
    def get_ingredients(self,food):
        """

        :param food:
        :return:
        """
        try:
            ingredients=self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        if ingredients!=False:
            return ingredients