from day12.workk.work3 import MoneyException

class Bank:
    __money = None

    def setmoney(self,money):
        self.__money = money

    def getmoney(self):
        return self.__money

    def draw_money(self,draw_money):
        if draw_money > 3000:
            raise MoneyException("金额不足")

        else:
            self.__money = self.__money - draw_money
            print("现在余额为：",self.getmoney())

try:
    b = Bank()
    b.setmoney(3000)
    b.draw_money(2900)
except MoneyException as i:
    print(i)


