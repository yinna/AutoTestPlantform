import requests
import json

class requestUtils():
    def __init__(self):
        self.baseUrl = "http://mall.ectpp.opsmart.cn"
        self.baseAdminUrl = "http://admin.ectpp.opsmart.cn"
        self.adminName = "pogba.ye"
        self.adminPwd = "Change_name22"
        

    def getECTIMGCAPTCHA(self):
        form_header = {"Cookie": "Hm_lvt_64241f86cc8a1671e8198f36599bf7d0=1560562861,1561170036,1561338563,1561772753; Hm_lpvt_64241f86cc8a1671e8198f36599bf7d0=1562667353"} 
        responseAll = requests.get(self.baseUrl+"/api/common/captcha/image?d=1562668357141",headers=form_header)
        clientHeader = responseAll.headers
        setCookie = str(clientHeader['Set-Cookie'])
        ECTIMGCAPTCHA = setCookie[14:50]
        return ECTIMGCAPTCHA
    
    def adminLogin(self):
        form_header = {"Content-Type": "application/json;charset=UTF-8","ECTIMGCAPTCHA":requestUtils().getECTIMGCAPTCHA()}
        responseLogin = requests.post(self.baseAdminUrl+"/api/admin/internal/user/login",headers=form_header,params='username=pogba.ye&password=Change_name22&domain=cn&')
        adminToken = responseLogin.headers['X-Auth-Token']
        requestUtils().setChinaTenant(adminToken)
        return adminToken

    def setChinaTenant(self,adminToken):
        form_header = {"Content-Type": "application/json;charset=UTF-8","X-Auth-Token":adminToken}
        requests.put(self.baseAdminUrl+"/api/admin/internal/user/update-internal-shared-user-by-tenant/a63727e57aaa2660e0539fe716acc5ab",headers=form_header)

    def cityEntityInfo(self,cityNameEnOrCn):
        form_header = {"Content-Type": "application/json;charset=UTF-8","X-Auth-Token":requestUtils().adminLogin()}
        jsonParams = {"cityName":cityNameEnOrCn,"unlocode":None}
        responseCity = requests.post(self.baseAdminUrl+"/api/common/city/search?page=0&size=20",headers=form_header,json=jsonParams)
        contentJson = json.loads(responseCity.text)
        cityEntityInfo = contentJson['content'][0]
        print(cityEntityInfo)
        return cityEntityInfo

    def portEntityInfo(self,portNameEnOrCn):
        form_header = {"Content-Type": "application/json;charset=UTF-8","X-Auth-Token":requestUtils().adminLogin()}
        jsonParams = {"portName":portNameEnOrCn,"portCode":None}
        responsePort = requests.post(self.baseAdminUrl+"/api/common/port/search?page=0&size=20",headers=form_header,json=jsonParams)
        contentJson = json.loads(responsePort.text)
        portEntityInfo = contentJson['content'][0]
        print(portEntityInfo)
        return portEntityInfo

if __name__ == "__main__":
    requestUtils().portEntityInfo("shekou")