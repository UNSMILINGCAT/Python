class Fridge(object):
    def __init__(self,items={}):
        self.items=items
    def _add_multi(self,food_name,quantity):
        """
        添加食物，首先进行检测，如果没有存在，则直接放入，如果存在，
        则进行数量上的相加
        """
        if(not food_name in self.items):
            self.items[food_name]=quantity
        else:
            self.items[food_name]=self.items[food_name]+quantity
        return
    
    def add_one(self,food_name):
        """
        """
        if type(food_name)!=type(""):
            raise TypeError ("add_one要求是一个字符串，"+
                             "无法传递一个%s" % type(food_name))
        else:
            self._add_multi(food_name,1)
            
        return True
    def add_many(self,food_dict):
        """
        """
        if type(food_dict)!=type({}):
            raise TypeError("add_many要求参数为字典类型，不接受%s" % type(food_dict))
        for food in food_dict:
            self._add_multi(food,food_dict[food])
        return True
    def has(self,food_name,quantity=1):
        """
        """
        return self.has_various({food_name:quantity})
    def has_various(self,foods):
        """
        """
        try:
            for food in foods:
                if self.items[food]<foods[food]:
                    return False
                return True
        except KeyError:
            return False
