class Animal:
    __name = None

    def __init__(self,name):
        self.__name = name


    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

class Dog(Animal):

    def __init__(self,name):
        super().setName(name)

dog = Dog("旺财")
name = dog.getName()
print(name)

