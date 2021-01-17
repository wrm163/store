print("=========================欢迎来到海澜之家商城=================================")
print("===========================================================================")
print("衣服类型      码数       价格        风格        适用季节       材质         数量")
print("衬衫          L       158.0      商务正装        秋季         棉            20")
print("羽绒服        XL      650.0      青春休闲        冬季       聚酯纤维         15")
print("夹克         XXL      658.0      商务休闲        秋季        羊毛           30")
print("西装          XL      719.0      商务正装         秋冬        羊毛          20")
print("风衣         3XL      370.0      青春流行        秋冬       聚酯纤维         25")
print("针织衫        XL      318.0      青春休闲        秋冬        其它           15")
print("卫裤         XXL      139,0      潮流时尚        秋冬        其它           20")
print("总金额为：",(158*20+650*15+658*30+719*20+370*25+318*15+139*20),"￥")


Clothestype="衬衫"
yardage="L"
price=158.0
style="商务正装"
Applytoseason="秋季"
texture="棉"
quantity=20

Clothestype1="羽绒服"
yardage1="XL"
price1=650.0
style1="青春休闲"
Applytoseason1="冬季"
texture1="聚酯纤维"
quantity1=15

Clothestype2="夹克"
yardage2="XXL"
price2=658.0
style2="商务休闲"
Applytoseason2="秋冬"
texture2="羊毛"
quantity2=30

Clothestype3="西装"
yardage3="XL"
price3=719.0
style3="商务正装"
Applytoseason3="秋冬"
texture3="羊毛"
quantity3=20

Clothestype4="风衣"
yardage4="3XL"
price4=370.0
style4="青春流行"
Applytoseason4="秋冬"
texture4="聚酯纤维"
quantity4=25

Clothestype5="针织衫"
yardage5="XL"
price5=318.0
style5="青春休闲"
Applytoseason5="秋冬"
texture5="其它"
quantity5=15

Clothestype6="卫裤"
yardage6="XXL"
price6=139.0
style6="潮流时尚"
Applytoseason6="秋冬"
texture6="其它"
quantity6=20
print("衣服类型\t\t码数\t\t价格\t\t\t风格\t\t\t适用季节\t\t材质\t\t\t数量")
print(Clothestype,"\t\t",yardage,"\t\t",price,"\t",style,"\t\t",Applytoseason,"\t\t",texture,"\t\t",quantity)
print(Clothestype1,"\t\t",yardage1,"\t",price1,"\t",style1,"\t\t",Applytoseason1,"\t\t",texture1,"\t",quantity1)
print(Clothestype2,"\t\t",yardage2,"\t",price2,"\t",style2,"\t\t",Applytoseason2,"\t\t",texture2,"\t\t",quantity2)
print(Clothestype3,"\t\t",yardage3,"\t",price3,"\t",style3,"\t\t",Applytoseason3,"\t\t",texture3,"\t\t",quantity3)
print(Clothestype4,"\t\t",yardage4,"\t",price4,"\t",style4,"\t\t",Applytoseason4,"\t\t",texture4,"\t",quantity4)
print(Clothestype5,"\t\t",yardage5,"\t",price5,"\t",style5,"\t\t",Applytoseason5,"\t\t",texture5,"\t\t",quantity5)
print(Clothestype6,"\t\t",yardage6,"\t",price6,"\t",style6,"\t\t",Applytoseason6,"\t\t",texture6,"\t\t",quantity6)
print("总金额：",(price*quantity+price1*quantity1+price2*quantity2+price3*quantity3+price4*quantity4+price5*quantity5+price6*quantity6),"￥")

