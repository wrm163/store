'''
异常：
    如何产生异常？就是程序在运行过程中，发生一种不正常的情况，叫做程序异常
    异常如何解决？
        1.手动向上抛：raise 异常
            弊端：异常还是没有解决
        2.捕捉....解决
            这种方式其实已经解决了异常
            2.1 使用方式：将有可能出现问题的代码放在try...except代码块中间来进行监控
            如果有问题使用except来进行异常匹配
            2.2 优点：处理了异常



    如何自定义异常？
'''

li = [5,8,4,2,3,0]
def getNum(li,index):
    if index >= len(li):
        raise AttributeError("角标超出范围了，别瞎弄！") #手动抛出异常
    else:
        return li[index]

try:
    n = getNum(li,9) # --> IndentationError python解释器  -->  控制台：异常所在行数，什么异常，异常的解释
    print(n)
except IndexError: # 匹配异常
    print("您访问的角标不存在，请重新输入！") #异常的处理代码
except IndentationError:
    print("其它异常！") #异常处理代码
except ArithmeticError:
    print("笨蛋，这么简单的算数都有问题！")
except Exception:
    print("这就是父类异常！")