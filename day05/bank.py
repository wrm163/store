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
#入口程序
while True:
    print(welcom)
    chose=input("请输入您的选项")
    if chose=="1":      #开户
        addUser()
    elif chose=="2":
        pass
    elif chose=="3":
        pass
    elif chose=="4":
        pass
    elif chose=="5":
        pass
    elif chose=="6":#退出
        print("拜拜了，您嘞！")
        break
    else:
        print("您输入的选项不存在")