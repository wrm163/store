shop=[
    ["IPhon8p",1000],
    ["Mac lopto",12000],
    ["Iwatch",500],
    ["lenovo pc",4000],
    ["辣条",10],
    ["洗衣粉",23.5],
]
while True:
    salary=input("请输入您的薪资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("请输入合适的薪资！")
mycart=[]

while True:
    import random
    a=(int(random.random() * 100))
    # discount = round((random.random() + 8) / 10, 2)
    print("----------欢迎来到小王商城---------")
    for item,value in enumerate(shop):
        print(item,value)
    chose=input("请输入要买的商品编号：")
    if chose.isdigit():
        chose=int(chose)
        if chose>=len(shop):
            print("\033[41;20;1m您输入的商品不存在!\033[0m")
        else:
            if salary<shop[chose][1]:
                print("\033[41;20;1m您的余额不足\033[0m")
            elif shop[chose][1]<5000:
                print("您本次积分为：200")
            elif shop[chose][1]>10000:
                print("您本次积分为：400")
            mycart.append(shop[chose])
            salary=salary-(shop[chose][1]-a)
            print("\033[32;20;1m购买成功！本次消费为：",salary,"本次优惠:",a,"\033[0m")
    elif chose=="Q" or chose=="q":
        break
    else:
        print("您输入不合法，请重新输入")
print("-----------欢迎下次光临xx商店-------------")
print("以下是您购买的商品",mycart)