class Chef:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name

    def getName(self):
        return  self.__name

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return  self.__age

    def rice(self,rice):
        print(self.__age ,"岁的",self.__name,"大厨，正在做",rice)

class Son(Chef):

    def cook(self,num):
        print("炒",num)
    def rice(self,rice):
        super().rice(rice)


class Grandson(Son):
    def cook(self,num):
        print("炒",num)
    def rice(self,rice):
        super().rice(rice)
son = Son()
son.setName("张三")
son.setAge(21)
son.rice("米饭")
son.cook("土豆丝")
s = Grandson()
s.setAge(10)
s.setName("李四")
s.rice("米饭")
s.cook("鱼香肉丝")




