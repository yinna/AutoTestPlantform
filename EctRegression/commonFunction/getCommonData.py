import cx_Oracle

from commonFunction import readConfig   #  整个框架跑脚本时
# import readConfig   #  调试时,不然会报错

class databaseUtils():
    def __init__(self):
        readConfig.configUtils().getEnvInfo("pp_db","username")
        self.conn = cx_Oracle.connect('ECT_OWNER',"Mm*cuN7V/U=\'fZVd",'172.32.231.249:1521/oraods',encoding="UTF-8")
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()

    #获取城市UUID，大小写匹配
    def getCityId(self,cityEnFullName):
        #使用execute方法执行SQL语句
        self.cursor.execute("SELECT UUID FROM CMN_CITY WHERE CITY_FULL_NAME_EN =\'" + cityEnFullName + "\'")
        result = self.cursor.fetchall()
        cityId = result[0][0]
        print('查询城市：'+cityEnFullName + '--UUID的值是：'+ cityId)
        return cityId

    #获取港口UUID,
    def getPortId(self,portEnFullName):
        #使用execute方法执行SQL语句
        self.cursor.execute("SELECT UUID FROM CMN_PORT WHERE PORT_FULL_NAME_EN =\'" + portEnFullName + "\'")
        result = self.cursor.fetchall()
        portId = result[0][0]
        print('查询港口：'+portEnFullName + '--UUID的值是：'+ portId)
        return portId

    def getProducts(self,commodityCode):
        print("111")

    def getCompanyId(self,companyNameZh):
        self.cursor.execute("SELECT ID FROM COMPANY c WHERE c.NAME_ZH =\'" + companyNameZh + "\'")
        result = self.cursor.fetchall()
        companyId = result[0][0]
        print("company--"+companyNameZh+"的id是："+companyId)
        return companyId

    def getUserId(self,username):
        self.cursor.execute("SELECT ID FROM user2 WHERE USERNAME =\'" + username + "\'")
        result = self.cursor.fetchall()
        userId = result[0][0]
        print("用户--" + username + "的id是：" + userId)
        return userId

if __name__ == "__main__":
    databaseUtils().getCityId("Shanghai")

