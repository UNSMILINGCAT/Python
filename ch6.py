import ch6_exercises
fridge=ch6_exercises.Fridge()
fridge.add_one("番茄")
print(fridge.items)
food_dict={"番茄":3,"土豆":2}
fridge.add_many(food_dict)
print(fridge.items)
print(fridge.has_various({"番茄":2,"土豆":2}))