a=[2,4,6,7,5,9]
b=0
for i in range(0,6):
    b=(b+a[i])
print("总和为：",b)

c=0
for i in range(0,6):
    if a[i]%2==0:
        c=(c+a[i])
print("偶数和为：",c)

d=0
for i in range(0,len(a)):
    if d<a[i]:
        d=a[i]
print("最大值为",d)