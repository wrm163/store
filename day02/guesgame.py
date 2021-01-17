import random
num=int(random.random()*100)
while True:
    a=int(input("请输入您要猜的数字："))
    if a>num:
        print("大了")
    elif a<num:
        print("小了")
    else:
        print("恭喜，猜中了，本次随机数为：",a)
