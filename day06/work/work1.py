class Counter:
    __num = None

    def plus(self,num1,num2):
        return num1 + num2

    def minus(self,num1,num2):
        return num1 - num2

    def ride(self,num1,num2):
        return num1 * num2

    def divide(self,num1,num2):
        return num1 / num2

counter = Counter()
while True:
    num1 = float(input("输入第一个数："))
    num2 = float(input("请输入第二个数："))
    choose = float(input("请选择计算方式：1.加  2.减  3.乘  4.除  请输入："))
    if choose == 1:
        print(counter.plus(num1,num2))
    elif choose == 2:
        print(counter.minus(num1,num2))
    elif choose == 3:
        print(counter.ride(num1,num2))
    elif choose == 4:
        print(counter.divide(num1,num2))
    else:
        print("输入不正确请重新输入！")
    break

# class Counter:
#     __num = None
#
#     def plus(self,num1,num2):
#         self.__num = num1 + num2
#         print(self.__num)
#
#     def minus(self,num1,num2):
#         self.__num = num1 - num2
#         print(self.__num)
#
#     def ride(self,num1,num2):
#         self.__num = num1 * num2
#         print(self.__num)
#
#     def divide(self,num1,num2):
#         self.__num = int(num1 / num2)
#         print(self.__num)
#
# counter = Counter()
# counter.plus(1,1)
# counter.minus(1,1)
# counter.ride(1,1)
# counter.divide(6,2)