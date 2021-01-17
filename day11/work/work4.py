class People:
    age = None
    sex = None
    name = None

class worker(People):
    def work(self):
        print(self.age,"岁",self.sex,self.name,"在工厂干活")

class student(People):

    num =None
    def study(self):
        print(self.age,"岁,",self.sex,",",self.name,",","学号为：",self.num,",的小孩在学习")
    def sing(self):
        print(self.age,"岁,",self.sex,",",self.name,",","学号为：",self.num,",的小孩在唱歌")


Worker = worker()
Worker.age = 12
Worker.sex = "女"
Worker.name = "李四"
Worker.work()

Student = student()
Student.age = 12
Student.sex = "男"
Student.name = "张三"
Student.num = 1
Student.study()
Student.sing()


# Student = student()
# Student.age = 12
# Student.sex = "男"
# Student.name = "张三"
# Student.num = 1
# Student.sing()