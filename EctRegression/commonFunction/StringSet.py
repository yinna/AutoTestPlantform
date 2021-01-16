class stringUtils():
    def __init__(self):
        pass

    # 脚本里面调用时，还得传3个参数
    def joinString(self,time,type,strJoin=None):
        if(str(type)=="start"):
            value = str(time) + "T00:00:00.000Z"
        if(str(type) == "end"):
            value = str(time) + "T23:59:59.000Z"
        if(str(type) == "join"):
            value = str(time) + str(strJoin)
            print("拼接时间为："+value)
        return value

if __name__ == "__main__":
    stringUtils().joinString(12,"join","fgd")