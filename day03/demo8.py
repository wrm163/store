list = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
            c=list[j]
            list[j]=list[i]
            list[i]=c
print(list)