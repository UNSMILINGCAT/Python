import ch6_Fridge
import ch6_Omelet
import ch6_Recipe

recipe = ch6_Recipe.Recipe()
recipe.add("蛋炒饭", {"鸡蛋": 2})
o = ch6_Omelet.Omelet("乳酪", recipe)
fridge = ch6_Fridge.Fridge({"乳酪": 5, "牛奶": 4, "鸡蛋": 12})
o.get_ingredients(fridge)
o.mix(False)
o.make()
