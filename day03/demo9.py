list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
for i in range(0,len(list)):
    b=0
    for j in range(0,len(list)):
        if list[i]==list[j]:
            b=b+1
    print(list[i],"出现过",b,"次")