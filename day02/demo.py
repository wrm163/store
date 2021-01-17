username="王瑞敏"
age=23
sex='女'
high=1.64
weigh=52
print("我叫",username,"，我今年",age,"岁","，我是",sex,"性","，我的身高",high,"，我的体重",weigh)

username="张三"
age=20
high=177
weigh=140

u1="李四"
age1=22
high1=166
weigh1=135

# 个人信息的打印模板
info='''
-------------个人展示-------------
姓名：{username}
年龄：{age}
身高：{high}
体重：{weigh}
---------------------------------
'''

print(info.format(username=username,age=age,high=high,weigh=weigh))
print(info.format(username=u1,age=age1,high=high1,weigh=weigh1))

info='''
-------------------个人展示-------------------
姓名：         年龄：      身高：         体重：
{username}    {age}      {high}      {weigh}

---------------------------------------------
'''
print(info.format(username=username,age=age,high=high,weigh=weigh))
