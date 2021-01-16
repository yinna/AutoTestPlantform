import configparser
import os

class configUtils():
    config_file_path = os.path.join("D:\\workspace\\EctRegression\\config","env.ini") #获取ini文件所在的路径
    def __init__(self,config_file_path=config_file_path):
        self.conf = configparser.ConfigParser() # 命名一个ConfigParser的类对象
        self.config_file_path = config_file_path
        self.conf.read(config_file_path,encoding="utf-8") # 读取整个config文件

    def getEnvInfo(self,section,key):
        value = self.conf.get(section,key)
        
        print('第二种方法读取到的值：',value)
        return value

if __name__ == "__main__":
    configUtils().getEnvInfo('pp','cnPrimaryUserAccount')