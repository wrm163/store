a=input("请输入姓名：")
b=int(input("请输入身份证号码:"))
c=int(input("请输入年龄:"))
d=input("请输入性别:")
e=input("请输入身高:")
f=input("请输入体重:")

info='''
姓名:{name},
身份证号:{IDnumber},
年龄:{age}岁,
性别:{sex},
身高:{high},
体重:{weight},
'''
print(info.format(name=a,IDnumber=b,age=c,sex=d,high=e,weight=f))