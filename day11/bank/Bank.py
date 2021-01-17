from day09.b.DBUtils import DBUtils
from day09.b.View import user_info
import time
class Bank:
    __db = DBUtils()
    __bankName = "中国工商银行北京市沙河支行"

    def getBankName(self):
        return self.__bankName

    def bankAddUser(self,user):
        sql1 = "select count(1) from t_user"  # 查询是否已满的数据库
        sql = "select * from t_user where account = %s" # 检查是否存在该用户
        sql2 = "insert into t_user(" \
               "account,username,password,country," \
               "province,street,door,money,reg_date,bankname)" \
               " values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param = [user.getAccount()]
        if self.__db.select(sql1,None)[0][0] >= 100:
            return 3
        elif len(self.__db.select(sql,param)) != 0:
            return 2
        else:
            param1 = [
                user.getAccount(),
                user.getUsername(),
                user.getPassword(),
                user.getAddress().getCountry(),
                user.getAddress().getProvince(),
                user.getAddress().getStreet(),
                user.getAddress().getDoor(),
                user.getMoney(),
                user.getBankName()
            ]
            self.__db.update(sql2,param1)

            print(user_info.format(account=user.getAccount(),
                          username=user.getUsername(),
                          password=user.getPassword(),
                          country=user.getAddress().getCountry(),
                          province=user.getAddress().getProvince(),
                          street=user.getAddress().getStreet(),
                          door=user.getAddress().getDoor(),
                          money=user.getMoney(),
                          time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                          bank_name=user.getBankName()))
            self.__db.releaseConnection()
            return 1

    def selectUser(self,account,password):
        sql = "select * from t_user where account = %s  and password = %s"
        param = [account,password]
        result = self.__db.select(sql,param,mode="one")
        return result

    def bankSaveMoney(self, account, money):
        sql = "select * from t_user where username = %s"
        sql2 = "select money from t_user where account = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        a = self.__db.select(sql,param)
        if len(a) != 0:
            return 2
        else:
            a = self.__db.select(sql2, param, mode="one")
            a = a[0] + money
            param1 = [a,account]
            self.__db.update(sql3, param1)
            return True

    def bankGetMoney(self, account, password, money):
        sql = "select * from t_user where account = %s"
        sql1 = "select * from t_user where account = %s  and password = %s"
        sql2 = "select money from t_user where account = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        param1 = [account,password]
        a = self.__db.select(sql2, param, mode="one")
        if len(self.__db.select(sql,param)) == 0:
            return 1
        elif len(self.__db.select(sql1, param1)) != 0:
            if a[0] < money:
                return 3
            else:
                b = a[0] - money
                param2 = [b,account]
                self.__db.update(sql3, param2)
                return 0
        else:
            return 2

    def bankMoveMoney(self, account, password, accound1, money):
        sql = "select * from t_user where account = %s "
        sql1 = "select * from t_user where account = %s  and password = %s"
        sql2 = "select money from t_user where account = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        param1 = [accound1]
        param2 = [account, password]
        a = self.__db.select(sql2, param, mode="one")
        c = self.__db.select(sql2, param1, mode="one")
        if len(self.__db.select(sql,param)) != 0 and len(self.__db.select(sql,param1)) != 0:
            if len(self.__db.select(sql1,param2)) != 0:
                if a[0] < money:
                    return 3
                else:
                    b = a[0] - money
                    d = c[0] + money
                    param3 = [b, account]
                    param4 = [c, accound1]
                    self.__db.update(sql3, param3)
                    self.__db.update(sql3,param4)
                    return 0
            else:
                return 2
        else:
            return 1


    def selectUser1(self, account, password):
        bank = Bank()
        sql = "select * from t_user where account = %s "
        sql1 = "select * from t_user where account = %s  and password = %s"
        param = [account]
        param1 = [account, password]
        if len(self.__db.select(sql,param)) == 0:
            print("账号不存在！")
        elif len(self.__db.select(sql1, param1)) == 0:
            print("账号密码错误！")
        else:
            database = bank.selectUser(account, password)
            print(user_info.format(account=database[1],
                                   username=database[2],
                                   password=database[3],
                                   country=database[4],
                                   province=database[5],
                                   street=database[6],
                                   door=database[7],
                                   money=database[8],
                                   time=database[9],
                                   bank_name=database[10]))

