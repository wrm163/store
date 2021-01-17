'''
老手机;
    打电话、来电号码、归属地、姓名、来电铃声

新手机：
    打电话、来电号码、归属地、姓名、来电铃声、大头贴
'''
import time
class Oldphone:
    number = None
    def call(self,number1):
        print(self.number,"正在打电话","打给",number1,"归属地：张家口，姓名：小王，来电铃声：叮叮当。。。")
        for i in range(6):
            print(".",end="")
            time.sleep(1)


class Newphone(Oldphone):
    def call(self,number1):
        super().call(number1) # 老手机功能照样用
        print("大头贴","小白兔") # 新手机功能

phone = Newphone()
phone.number = "18910553447"
phone.call("17600044774")


# class Newphon:
#     def call(self,number):