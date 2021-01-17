for i in range(0,10,2):
    print(i)

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",(j*i),"\t",end="")
    print()