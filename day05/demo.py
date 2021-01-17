provinces={
    "010":"北京",
    "020":"上海",
    "030":"广州",
    "040":"深圳",
}
#如何取数据
value=provinces["010"]
print(value)
#添加 050天津
provinces["050"]="天津"
print(provinces)
#如何遍历数据
keys=provinces.keys()
for key in keys:
    print(key,"=",provinces[key])

# 迁到安徽 修改010对应的位置
provinces["010"]="安徽"
print(provinces)










