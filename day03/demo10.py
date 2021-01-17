# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]
a=0
for i in range(0,len(names)):
    a=a+names[i][5]
    print("每人平均薪资为：",a/len(names))

age=0
for j in range(0,len(names)):
    age=age+int(names[j][1])
    print("每个人平均年龄为：",age/len(names))

names.append(["张佳伟",45,"男","220","alibaba",500,30])
print(names)

men=0
women=0
for h in range(0,len(names)):
    if names[h][2]=='男':
        men=men+1
    else:
        women=women+1
print("男生的人数为：",men,"女生的人数为：",women)

a1=0
b1=0
c1=0
d1=0
for k in range(0,len(names)):
    if names[k][6]=="50":
        a1=a1+1
    elif names[k][6]=="60":
        b1=b1+1
    elif names[k][6]=="10":
        c1=c1+1
    elif names[k][6]=="30":
        d1=d1+1
print("50部门的人数为:",a1,"\t","60部门的人数为:",b1,"\t","10部门的人数为:",c1,"\t","30部门的人数为:",d1)