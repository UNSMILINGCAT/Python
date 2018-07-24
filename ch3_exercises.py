dairy_section=["新鲜奶酪","柔皮白奶酪","山羊奶酪","蓝奶酪"];
print("%s %s" % (dairy_section[0],dairy_section[1]));
milk_expiration=(12,10,2009);
print("This milk carton will expire on %d/%d/%d"%(milk_expiration[0],milk_expiration[1],milk_expiration[2]));
milk_carton={"expiration_date":milk_expiration,"fl_oz":"15x15","Cost":15,"brand_name":"蒙牛"}
print(milk_carton)
print("6罐牛奶的价格为：%s = %d"%(str(milk_carton["Cost"])+" x 6",milk_carton["Cost"]*6));
cheeses=["半硬质奶酪","硬质奶酪","加工奶酪"]
dairy_section.append(cheeses)
print(dairy_section)
dairy_section.pop()
print(dairy_section)
print(len(cheeses))
print("第一个奶酪名称的前五个字母是：%s"%(cheeses[0][0:5]))
