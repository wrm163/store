a= [3,6,5,2,7,1,8,4,9]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            c=a[j]
            a[j]=a[i]
            a[i]=c
print(a)
