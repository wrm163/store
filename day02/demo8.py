a=int(input("第一条边输入："))
b=int(input("第二条边输入："))
c=int(input("第三条边输入："))
if a+b>c and b+c>a and a+c>b :
    if a==b and a!=c:
        print("等腰三角形")
    elif b==c and a!=b:
        print("等腰三角形")
    elif a==c and a!=b:
        print("等腰三角形")
    elif a==b and b==c and a==c:
            print("等边三角形")
    else:
        print("构成普通三角形")
else:
    print("不构成三角形")


