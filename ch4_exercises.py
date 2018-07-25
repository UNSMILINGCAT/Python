for i in range(5) :
    print("%d 是 %s" %(i,i==True))

while True:
    
    #一个获取键盘输入语句
    num=input("请输入一个数字：")
    num=int(num)
    if(num>=0 and num<=9):
        print("%d"% num)
    elif(num<0):
        break
demo_sequence=["王林","李慕婉"]
if("王"==demo_sequence[0]):
    print("在序列的第一个位置")
elif("王"==demo_sequence[1]):
    print("位于序列的第二个位置")
else:
    print("不处于当前序列")


fridge={"土豆":"土豆可以作为主食使用，含丰富的淀粉","番茄":"番茄富含维生素，多多使用"
        ,"胡萝卜":"胡萝卜含有大量的胡萝卜素，对眼睛会好点"}
food_sought="胡萝卜"
for food in fridge:
    if(food==food_sought):
        print(fridge[food])
        #break
else:
    print("元素没有找到食物的消息")

fridge_list=[]
fridge_list.extend(fridge.keys())
while len(fridge_list)>0:
    current_key=fridge_list.pop()
    try :
        print(fridge[current_key])
    except (KeyError) as error:
        print("没有找到%s这个键"%error)
    
else:
    print("匹配结束，退出循环")


try:
    print(fridge["土豆1"])
except (KeyError)as error:
    print("没有找到%s这个键"% error)
