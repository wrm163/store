'''
有比较的方法：
如果两个人名字和年龄相同则是同一个人
否则，抛出异常姓名或年龄不匹配
'''
from day12.UserException import UserNotExistsException

class User:
    __username = None
    __age = None

    def __init__(self,username,age):
        self.__username = username
        self.__age = age

    def setusername(self,username):
        self.__username = username

    def getusername(self):
        return self.__username

    def setage(self,age):
        self.__age  = age

    def getage(self):
        return self.__age

    # 比较两个人的方法

    def comper(self,user):
        if self.__username == user.getusername() and self.__age == user.getage():
            print("同一个人")
        else:
            raise  UserNotExistsException("姓名或年龄不匹配。")
try:
    u1 = User("张三",1)
    u2 = User("张三",12)
    u1.comper(u2)
except Exception as a: # as重新命名，后面名字可以随便起
    print("姓名或年龄不匹配",a)