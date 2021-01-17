from day09.b.Address import Address
from day09.b.Bank import Bank
from day09.b.Utils import Utils
class User:
    __account = None
    __username = None
    __password = None
    __money = None
    __address = None
    __registerDate = None
    __bankName = None



    def __init__(self,username="",password="",money="",address=""):
        self.__account = Utils().getRandom()
        self.__password = password
        self.__money = money
        self.__bankName = Bank().getBankName()
        self.__username = username
        self.__address =  address
        self.__registerDate = "now()" # 对应的数据库的now() 函数

    def setAccount(self,account):
        self.__account = account

    def getAccount(self):
        return self.__account

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    # def setRegisterDate(self, registerDate):
    #     self.__registerDate = registerDate

    def getRegisterDate(self):
        return self.__registerDate

    # def setBankName(self, bankName):
    #     self.__bankName = bankName

    def getBankName(self):
        return Bank().getBankName()