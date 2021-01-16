class listUtils():
    def __init__(self):
        pass

    # 脚本里面调用时，还得传3个参数
    def listLength(self,*listEntry):
        length = len(listEntry)
        print(listEntry,"list长度",length)
        return length

if __name__ == "__main__":
    list = ['physics', 'chemistry', 1997, 2000]
    listUtils().listLength(*list)