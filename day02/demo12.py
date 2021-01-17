i=0
while True:
    i=i+1
    A=input("请输入用户名：")
    B=input("请输入密码：")
    if A=="jason" and B=="admin":
        print("登录成功！")
    elif i==3:
        print("密码已锁定")
        break
    else:
        print("用户名或密码错误！")
