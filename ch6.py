from ch6 import *

recipe = Recipe()
recipe.add("蛋炒饭", {"鸡蛋": 2})
o = Omelet("乳酪", recipe)
fridge = Fridge({"乳酪": 5, "牛奶": 4, "鸡蛋": 12})
o.set_kind("蛋炒饭")
o.get_ingredients(fridge)
o.mix(False)
o.make()
