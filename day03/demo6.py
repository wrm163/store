a=[15,20,12,63,3,8,94,61,27,5,10]
b=0
for i in range(0,len(a)):
    if a[i]%5==0:
        b=b+a[i]
print("5的倍数之和为：",b)