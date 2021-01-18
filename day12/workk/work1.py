from day12.workk.work import AgeException

class Person:
    __age = None

    def setage(self,age):
        # if age <= 0:
        #     raise AgeException("输入数据不正确，请重新输入")
        self.__age = age
        # else:
        #     self.__age = age
        #     print("数据合法！")

    def getage(self):
        return self.__age

    def num(self):
        if self.getage() > 0:
            print("您的年龄为：",self.getage())
        else:
            raise AgeException("输入数据不正确，请重新输入")
try:
    p = Person()
    p.setage(8)
    p.num()
except AgeException as E:
    print(E)




