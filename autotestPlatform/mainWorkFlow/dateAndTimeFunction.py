import time
import datetime

# 获取当前时间
def automationResultTime():
    current = datetime.datetime.now().strftime('%Y%m%d')
    return current

#  生成当前时间13位时间戳
def currenttimestamp():
    millis = int(round(time.time() * 1000))
    return millis

#  生成当前时间年月日时分秒格式
def currentTimeYMdHMS():
    current = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return current

#  生成当前时间年月日时分秒格式
def currentTimeY_M_dHMS():
    current = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current

#  生成当前时间年-月-日格式
def currentTimeY_M_d():
    current = datetime.datetime.now().strftime('%Y-%m-%d')
    return current

if __name__ == '__main__':
    print(currentTimeY_M_dHMS())
