class Oldphone:
    __brand = None

    def setbrand(self,brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def Call(self,name):
        print("正在给",name,"打电话。。。")


class Newphone(Oldphone):
    def Doal(self,name):
        print("语音拨号中。。。。")
        super().Call(name)
        print("品牌为：",self.getbrand(),"的手机很好用。。。")


newphone = Newphone()
newphone.setbrand("三星")
newphone.Doal("张三")

