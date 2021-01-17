# author:wrm02
import random
#银行库
bank={}
#银行的名称
bank_name="中国工商银行昌平支行"
#欢迎模板
welcom='''
****************************
*   中国工商银行账户管理系统    *
****************************
*   1、开户                 *
*   2、存钱                 *
*   3、取钱                 *
*   4、转账                 *
*   5、查询                 *
*   6、拜拜                 *
****************************
'''

#随机8位取号
def getrandom():  #def随意定义一个值
    li=['1','2','3','4','5','6','7','8','9','0']
    string=""
    for i in range(8):
        index=int(random.random()*len(li))
        string=string+li[index]
    return string  #return的意思是返回数据给定义的值

#银行的开户逻辑
def bank_addUser(username,password,country,province,street,door,money,accont):
    if len(bank)>=100:
        return 3
    elif accont in bank:
        return 2
    else:
        bank[accont]={
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name,
        }
        return 1

#开户逻辑
def addUser():#sddUser意思是"添加用户"
    username=input("请输入您的姓名：")
    password=input("请输入您的密码：")
    print("接下来请输入您的地址：")
    country=input("国家：")
    province=input("省份：")
    street=input("街道：")
    door=input("门牌号")
    money=input("请输入余额：")
    accont=getrandom()  #账号是随机获取的
    # print(username,password,country,province,street,door,money,accont)
    #将上述数据传输到银行开户逻辑
    status=bank_addUser(username,password,country,province,street,door,money,accont)
    if status==3:
        print("对不起，本行用户库已满，请您携带证件到其它银行办理")
    elif status==2:
        print("对不起，你输入的个人信息已经存在，请稍候再试！")
    elif status==1:
        print("恭喜你，开户成功！以下是您的开户信息")
        info='''
            --------------开户信息----------------
            账号:{accont}
            姓名:{username}
            密码:{password}
            地址信息：
                国家:{country}
                省份:{province}
                街道：{street}
                门牌号:{door}
            余额:{money}
            开户行:{bank_name}
            -------------------------------------
        '''
#获取银行的个人信息
        user= bank[accont]
        print(info.format(accont=accont,
                      username=user["username"],
                      password=user["password"],
                      country=user["country"],
                      province=user["province"],
                      street=user["street"],
                      door=user["door"],
                      money=user["money"],
                      bank_name=user["bank_name"]))

#银行查询逻辑
def bank_find(accont,passwork):
    return 0

#查询逻辑
def find():
    accont=input("请输入您的账号：")
    if accont in bank:
        pass
        password = input("请输入您的密码：")
        if bank[accont]["password"]==password:
            print("以下是您的查询信息：")
            info = '''
                    --------------查询信息----------------
                    账号:{accont}
                    姓名:{username}
                    密码:{password}
                    地址信息：
                        国家:{country}
                        省份:{province}
                        街道：{street}
                        门牌号:{door}
                    余额:{money}
                    开户行:{bank_name}
                    -------------------------------------
                '''
            user = bank[accont]
            print(info.format(accont=accont,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))
        else:
            print("您输入的密码错误")
    else:
        print("您输入的账号错误")

#银行存款逻辑
def bank_savemoney(accont):
    if accont in bank:
        return True
    else:
        return False
#存款逻辑
def savemoney():
    accont=input("请输入您的账号：")
    money1=input("请输入您要存的金额：")
    while True:
        if money1.isdigit():
           money1=int(money1)
           break
        else:
            print("输入非法！请重新输入")
            money1 = input("请输入您要取的金额：")
    status=bank_savemoney(accont)
    if status==False:
        print("您输入的账号不存在！")
    else:
        money2=int(bank[accont]["money"])+int(money1)
        print("您现在的余额为:",money2,"存入金额为：",money1)

#银行取款逻辑
def bank_getmoney(accont,password,money):
    if accont in bank:
        pass
        if password==bank[accont]["password"]:
            pass
            if int(bank[accont]["money"])>money:
                pass
            else:
                return 3
        else:
            return 2
    else:
        return 1
#取款逻辑
def getmoney():
    accont=input("请输入您的账号：")
    password=input("请输入您的密码：")
    money=input("请输入您要取的金额：")
    while True:
        if money.isdigit():
           money=int(money)
           break
        else:
            print("输入非法！请重新输入")
            money = input("请输入您要取的金额：")
    status = bank_getmoney(accont,password,money)
    if status==1:
        print("您输入的账号不存在!")
    elif status==2:
        print("您输入的密码不正确！")
    elif status==3:
        print("您的余额不足！")
    else:
        money1=int(bank[accont]["money"])-money
        print("取款成功，您现在余额为：",money1,"取款金额为：",money)

#银行转账逻辑
def bank_movemoney(accont,password,accont1,money):
    if accont in bank and accont1:
        pass
        if bank[accont]["password"]==password:
            pass
            if int(bank[accont]["money"])>=money:
                pass
                if accont1 in bank:
                    pass
                    if accont==accont1:
                        return 5
                else:
                   return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1
#转账逻辑
def movemoney():
    accont=input("请输入您的账号：")
    password=input("请输入您的密码：")
    accont1=input("请输入您要转入的账号：")
    money=input("请输入您要转出的金额：")
    while True:
        if money.isdigit():
           money=int(money)
           break
        else:
            print("输入非法")
            money = input("请输入您要转出的金额：")
    status =bank_movemoney(accont,password,accont1,money)
    if status==1:
        print("您的账号输入错误！")
    elif status==2:
        print("您输入的密码不正确！")
    elif status==3:
        print("您的余额不足！")
    elif status==4:
        print("您输入的转入账号错误！")
    elif status==5:
        print("您输入的账号一致，请重新输入！")
    else:
        money1=int(bank[accont]["money"])-money
        print("转账成功，您现在的余额为：",money1,"转出金额为：",money)
#入口程序
while True:
    print(welcom)
    chose=input("请输入您的选项")
    if chose=="1":      #开户
        addUser()
    elif chose=="2":
        savemoney()
    elif chose=="3":
        getmoney()
    elif chose=="4":
        movemoney()
    elif chose=="5":
        find()
    elif chose=="6":#退出
        print("拜拜了，您嘞！")
        break
    else:
        print("您输入的选项不存在")