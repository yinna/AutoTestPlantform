from mainWorkFlow import excelOperation
from mainWorkFlow import dateAndTimeFunction
import requests

global clientApiUrl,adminApiUrl,cb_inv_uuid,signBillBcNo,freeDNDBcNo,primaryUserName,password,subUserName,expiredUserName
clientApiUrl = excelOperation.readTestData("pp场",1,0)
adminApiUrl = excelOperation.readTestData("pp场",2,0)
cb_inv_uuid = excelOperation.readTestData("pp场",3,0)
signBillBcNo = excelOperation.readTestData("pp场",4,0)  #签单时BC_NO
freeDNDBcNo = excelOperation.readTestData("pp场",5,0)  #免箱天BC_NO
primaryUserName = excelOperation.readTestData("pp场",6,0) #主用户名称
password = excelOperation.readTestData("pp场",7,0)
subUserName = excelOperation.readTestData("pp场",8,0) #子用户名称
expiredUserName = excelOperation.readTestData("pp场",9,0) #过期浏览用户名称

global pass_count,fail_count,total_count
pass_count = 0
fail_count = 0
total_count = pass_count + fail_count

def getCaptcha():
    millis = dateAndTimeFunction.currenttimestamp()
    url = clientApiUrl+"/api/common/captcha/image?d=" + str(millis)
    r = requests.get(url)
    resp_headers = r.headers
    print("获取验证码的响应码",r.status_code)
    # 将头信息转为可以进行json序列化的
    x = requests.structures.CaseInsensitiveDict(resp_headers)
    # print js # 此处打印出来的是一个json字符串
    js = dict(x)
    # 获取其中json中的一个key值，并截取一部分
    ECTIMGCAPTCHA = js.get("Set-Cookie")[14:50]
    return ECTIMGCAPTCHA

def clientLogin(username,password):
    ECTIMGCAPTCHA = getCaptcha()
    url = clientApiUrl+"/api/admin/user/login"
    headers = {"conyent-type":"application/x-www-form-urlencoded","ECTIMGCAPTCHA":ECTIMGCAPTCHA}
    data = "username="+ username + "&password=" + password
    r = requests.post(url, params=data,headers=headers)
    # 获取请求头
    resp_headers = r.headers
    # 将头信息转为可以进行json序列化的
    x = requests.structures.CaseInsensitiveDict(resp_headers)
    # print js # 此处打印出来的是一个json字符串
    js = dict(x)
    # 获取其中json中的一个key值，并截取一部分
    clientToken = js.get("X-Auth-Token")
    return clientToken


# if __name__ == '__main__':
#     print(clientLogin(primaryUserName,password))