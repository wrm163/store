'''
继承：
被继承的类：父类。超类
继承的类：子类
在继承中如何使用父类的代码，super就是父类
'''
class Animal:  # 动物：父类
    name = None
    age = None

# 让狗、猫来继承动物
class Dog(Animal): # 子类
    def lookgeat(self): # 看大门
        print(self.name,"看大门","看了",self.age)

class Cat(Animal):
    def catchMouse(self):
        print(self.name,"正在抓老鼠")

dog = Dog()
dog.name = "哈士奇"
dog.age = 15
dog.lookgeat()
