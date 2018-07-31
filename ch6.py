import ch6_Fridge
import ch6_Omelet
o=ch6_Omelet.Omelet("乳酪")
fridge=ch6_Fridge.Fridge({"乳酪":5,"牛奶":4,"鸡蛋":12})
o.get_ingredients(fridge)
o.mix(False)
o.make()
a={"a":{"aa":1}}
print(a)
if not "a" in a:
    a["a"]={"n":2}
print(a)
