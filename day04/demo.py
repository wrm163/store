shop=[
    ["IPhon8p",1000],
    ["Mac lopto",12000],
    ["Iwatch",500],
    ["lenovo pc",4000],
    ["辣条",10],
    ["洗衣粉",23.5],
]
# for item,value in enumerate(shop):
#     print(item,value)

while True:
    salary=input("请输入您的薪资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("请输入合适的薪资！")
    #我的购物车，里面是空的
mycart=[]
#开始购物
while True:
    # 先展示商品
    print("---------------欢迎来到xxx商城--------------")
    for item,value in enumerate(shop):#enumerate枚举的意思，包含后面括号里的全部内容
        print(item,value)
    #请输入要买的商品编号
    chose=input("请输入要买的商品编号：")
    if chose.isdigit():#判断输入是不是数字
        chose=int(chose) #将数字转换成整型
        if chose>len(shop):
            print("\033[41;20;1m您输入的商品不存在!\033[0m")
        else:
            if salary<shop[chose][1]:#钱不够的时候，薪资小于购买商品的钱数
                print("\033[41;20;1m您的余额不足\033[0m")
            else:#正常买东西，添加到购物车，薪资减去相对应的商品金钱
                mycart.append(shop[chose])
                salary=salary-shop[chose][1]
                print("\033[32;20;1m购买成功！余额为：",salary,"\033[0m")
    elif chose=="Q" or chose=="q":
        break
    else:
        print("您输入不合法，请重新输入")
print("-----------欢迎下次光临xx商店-------------")
print("以下是您购买的商品",mycart)


