import time
from httprunner import __version__

from commonFunction import readConfig
from commonFunction import getCommonData
from commonFunction import timeOperation
from commonFunction import StringSet
from commonFunction import listOperation
from commonFunction import commonDataFromRequest


def get_httprunner_version():
    return __version__

#  登录获取时间戳timestamp
def getTimestamp():
    return int(round(time.time()*1000))

#  获取今天日期
def getCurrentDay():
    return timeOperation.timeUtils().currentDay()
def getDateAfterSomeDay(time_interval):
    return timeOperation.timeUtils().dateAfterSomeDay(time_interval)

#获取当前测试环境的用户、地址等信息
def getEnvInfo(section,key):
    value = readConfig.configUtils().getEnvInfo(section,key)
    return value

#等待几秒
def sleepTime(sec):
    time.sleep(int(sec))

#获取城市id
def getCityUuid(cityEnFullName):
    uuid = getCommonData.databaseUtils().getCityId(cityEnFullName)
    return uuid
#获取港口id
def getPortUuid(portEnFullName):
    uuid = getCommonData.databaseUtils().getPortId(portEnFullName)
    return uuid
# 获取公司ID
def getCompanyId(companyNameZh):
    companyId = getCommonData.databaseUtils().getCompanyId(companyNameZh)
    return companyId
#获取用户ID
def getUserId(username):
    userId = getCommonData.databaseUtils().getUserId(username)
    return userId

#获取城市实体信息
def getCityEntityInfo(cityNameEnOrCn):
    resultJson = commonDataFromRequest.requestUtils().cityEntityInfo(cityNameEnOrCn)
    return resultJson
#获取港口实体信息
def getPortEntityInfo(portNameEnOrCn):
    resultJson = commonDataFromRequest.requestUtils().portEntityInfo(portNameEnOrCn)
    return resultJson

def getJoinString(beforeStr,type,behindStr):
    return str(StringSet.stringUtils().joinString(beforeStr,type,behindStr))

# 获取list数组长度
def getListLength(*listEntry):
    length = listOperation.listUtils().listLength(*listEntry)
    return length

if __name__ == "__main__":
    getListLength(*["222","222"])