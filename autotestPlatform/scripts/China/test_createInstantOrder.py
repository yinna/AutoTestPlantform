# encoding:utf-8
import HTMLTestRunner
import json
import unittest

from assertpy import assert_that
import requests

from mainWorkFlow import excelOperation, dateAndTimeFunction
from mainWorkFlow import globalApiValueAndFunction


class test_createInstantOrder(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.primaryUserClientToken = globalApiValueAndFunction.clientLogin(globalApiValueAndFunction.primaryUserName, globalApiValueAndFunction.password)

    def setUp(self):
        self.g = globals()

    def test_queryExtraFee(self):
        url = globalApiValueAndFunction.clientApiUrl + "/api/common/feeUpload/searchfee"
        headers = {"conyent-type": "application/json;charset=UTF-8",
                   "X-Auth-Token": self.primaryUserClientToken}
        data = [
            {
                "key": 1,
                "effectiveTime": "2020-12-26T01:00:00.000Z",
                "chargeModel": "BOTH",
                "tradeAreaCode": "LATD",
                "tradeLaneCode": "AAW",
                "svcLoopCode": "AEU9",
                "direction": "W",
                "areaCode": "77c42f4af2d75052acee0c0aa87cbc83",
                "regionCode": "7fffffffea4b4571acb27fffffff7bc9",
                "por": "738872886232873",
                "pod": "349645770723668",
                "fnd": "738872886270322",
                "channelCode": "GENERAL",
                "cargoCategory": "GENERAL",
                "cntrInfo": [
                    {
                        "cntrSize": "40GP",
                        "amount": 1
                    },
                    {
                        "cntrSize": "40HQ",
                        "amount": 1
                    },
                    {
                        "cntrSize": "20GP",
                        "amount": 1
                    }
                ],
                "transhipmentPortIds": [],
                "paymentTerms": "P"
            }
        ]
        r = requests.post(url=url, json=data, headers=headers)
        # 获取响应码
        status_code = r.status_code
        assert_that(status_code).is_equal_to(200)
        # 转换成json
        response = json.loads(r.content)
        # 按票的附加费
        sizeBL = len(response[0]['chargeInfo'][0]['chargeDetail'])
        self.orderItemBLCharges = []
        if sizeBL >0:
            for i in range(sizeBL):
                self.orderItemBLCharge = {
                    "chargeName": response[0]['chargeInfo'][0]['chargeDetail'][i]['chargeName'],
                    "chargeCode": response[0]['chargeInfo'][0]['chargeDetail'][i]['chargeCode'],
                    "chargeType": response[0]['chargeInfo'][0]['chargeDetail'][i]['chargeType'],
                    "chargeHisId": response[0]['chargeInfo'][0]['chargeDetail'][i]['chargeHisId'],
                    "price": response[0]['chargeInfo'][0]['chargeDetail'][i]['price'],
                    "currency": response[0]['chargeInfo'][0]['chargeDetail'][i]['currency'],
                    "toCurrency": "CNY",
                    "transitPortId": response[0]['chargeInfo'][0]['chargeDetail'][i]['transhipmentPortId'],
                    "paymentTermsType": response[0]['chargeInfo'][0]['chargeDetail'][i]['paymentTerms'],
                    "include": response[0]['chargeInfo'][0]['chargeDetail'][i]['include']
                }
                self.orderItemBLCharges.append(self.orderItemBLCharge)
                self.g["orderItemBLCharges"] = self.orderItemBLCharges
            print(self.g["orderItemBLCharges"])

        # 20GP箱型的附加费
        size20GP = len(response[0]['chargeInfo'][1]['chargeDetail'])
        self.orderItem20GPCharges = []
        if size20GP > 0:
            for i in range(size20GP):
                self.orderItem20GPCharge = {
                    "chargeName": response[0]['chargeInfo'][1]['chargeDetail'][i]['chargeName'],
                    "chargeCode": response[0]['chargeInfo'][1]['chargeDetail'][i]['chargeCode'],
                    "chargeType": response[0]['chargeInfo'][1]['chargeDetail'][i]['chargeType'],
                    "chargeHisId": response[0]['chargeInfo'][1]['chargeDetail'][i]['chargeHisId'],
                    "price": response[0]['chargeInfo'][1]['chargeDetail'][i]['price'],
                    "currency": response[0]['chargeInfo'][1]['chargeDetail'][i]['currency'],
                    "toCurrency": "CNY",
                    "transitPortId": response[0]['chargeInfo'][1]['chargeDetail'][i]['transhipmentPortId'],
                    "paymentTermsType": response[0]['chargeInfo'][1]['chargeDetail'][i]['paymentTerms'],
                    "include": response[0]['chargeInfo'][1]['chargeDetail'][i]['include']
                }
                self.orderItem20GPCharges.append(self.orderItem20GPCharge)
            print(self.orderItem20GPCharges)
            self.orderItem20GPCharges.append(
                {"chargeName": "海运费", "chargeCode": None, "chargeType": "OCEAN_FEE", "price": 100, "currency": "USD",
                 "toCurrency": "CNY", "transitPortId": None, "paymentTermsType": "P"})
            globals()["orderItem20GPCharges"] = self.orderItem20GPCharges

        # 40GP箱型的附加费
        size40GP = len(response[0]['chargeInfo'][2]['chargeDetail'])
        self.orderItem40GPCharges = []
        if size40GP > 0:
            for i in range(size40GP):
                self.orderItem40GPCharge = {
                    "chargeName": response[0]['chargeInfo'][2]['chargeDetail'][i]['chargeName'],
                    "chargeCode": response[0]['chargeInfo'][2]['chargeDetail'][i]['chargeCode'],
                    "chargeType": response[0]['chargeInfo'][2]['chargeDetail'][i]['chargeType'],
                    "chargeHisId": response[0]['chargeInfo'][2]['chargeDetail'][i]['chargeHisId'],
                    "price": response[0]['chargeInfo'][2]['chargeDetail'][i]['price'],
                    "currency": response[0]['chargeInfo'][2]['chargeDetail'][i]['currency'],
                    "toCurrency": "CNY",
                    "transitPortId": response[0]['chargeInfo'][2]['chargeDetail'][i]['transhipmentPortId'],
                    "paymentTermsType": response[0]['chargeInfo'][2]['chargeDetail'][i]['paymentTerms'],
                    "include": response[0]['chargeInfo'][2]['chargeDetail'][i]['include']
                }
                self.orderItem40GPCharges.append(self.orderItem40GPCharge)
            print(self.orderItem40GPCharges)
            self.orderItem40GPCharges.append(
                {"chargeName": "海运费", "chargeCode": None, "chargeType": "OCEAN_FEE", "price": 200, "currency": "USD",
                 "toCurrency": "CNY", "transitPortId": None, "paymentTermsType": "P"})
            globals()["orderItem40GPCharges"] = self.orderItem40GPCharges

        # 40HQ箱型的附加费
        size40HQ = len(response[0]['chargeInfo'][3]['chargeDetail'])
        self.orderItem40HQCharges = []
        if size40HQ > 0:
            for i in range(size40HQ):
                self.orderItem40HQCharge = {
                    "chargeName": response[0]['chargeInfo'][3]['chargeDetail'][i]['chargeName'],
                    "chargeCode": response[0]['chargeInfo'][3]['chargeDetail'][i]['chargeCode'],
                    "chargeType": response[0]['chargeInfo'][3]['chargeDetail'][i]['chargeType'],
                    "chargeHisId": response[0]['chargeInfo'][3]['chargeDetail'][i]['chargeHisId'],
                    "price": response[0]['chargeInfo'][3]['chargeDetail'][i]['price'],
                    "currency": response[0]['chargeInfo'][3]['chargeDetail'][i]['currency'],
                    "toCurrency": "CNY",
                    "transitPortId": response[0]['chargeInfo'][3]['chargeDetail'][i]['transhipmentPortId'],
                    "paymentTermsType": response[0]['chargeInfo'][3]['chargeDetail'][i]['paymentTerms'],
                    "include": response[0]['chargeInfo'][3]['chargeDetail'][i]['include']
                }
                self.orderItem40HQCharges.append(self.orderItem40HQCharge)
                globals()["orderItem40HQCharges"] = self.orderItem40HQCharges
            print(self.orderItem40HQCharges)
            self.orderItem40HQCharges.append(
                {"chargeName": "海运费", "chargeCode": None, "chargeType": "OCEAN_FEE", "price": 300, "currency": "USD",
                 "toCurrency": "CNY", "transitPortId": None, "paymentTermsType": "P"})
        # 判断响应码是200，case就通过
        if r.status_code == 200:
            case_result = "通过"
        else:
            case_result = "失败"
        test_result = {"0": "产品附加费查询", "1":"响应码返回200", "2": "响应码200", "3": "响应码为" + str(r.status_code), "4": case_result}
        excelOperation.addDataToExistExcel("report", **test_result)

    def test_createInstantOrder(self):
        print(self.g['orderItemBLCharges'])
        url = globalApiValueAndFunction.clientApiUrl + "/api/product/client/order"
        headers = {"conyent-type": "application/json;charset=UTF-8",
                   "X-Auth-Token": self.primaryUserClientToken}
        data = {
            "order": {"prodId": "8aaacf6872b745a30172b74ba0550003", "prodType": "SAILING_PROD", "sailingProdType": "I",
                      "tradeLaneCode": "AAW", "channelCode": "GENERAL", "orderItems": [
                    {"itemType": "CNTR", "cntrType": "20GP", "quantity": 1, "orderItemCharges": globals()["orderItem20GPCharges"],
                     "cargoValue": 0},
                    {"itemType": "CNTR", "cntrType": "40GP", "quantity": 0, "orderItemCharges": globals()["orderItem40GPCharges"],
                     "cargoValue": 0},
                    {"itemType": "CNTR", "cntrType": "40HQ", "quantity": 0, "orderItemCharges": globals()["orderItem40HQCharges"],
                     "cargoValue": 0}, {"itemType": "BL", "quantity": 1, "orderItemCharges": self.g["orderItemBLCharges"]}],
                      "trailerServices": [], "transferServices": [], "paymentInfo": {}, "coupon": {},
                      "reeferValueAddServices": [], "paymentPercentage": 10, "totalPricePercentage": 10},
            "orderPromotionUsageParam": [], "operations": []}
        r = requests.post(url=url, json=data, headers=headers)
        result = json.loads(r.content)
        print(result)
        globals()["order_no"] = result['orderNo']
        # 判断响应码是200，case就通过
        if r.status_code == 200:
            case_result = "通过"
        else:
            case_result = "失败"
        test_result = {"0": "创建订单", "1": "响应码返回200", "2": "响应码200", "3": "响应码为" + str(r.status_code),
                       "4": case_result}
        excelOperation.addDataToExistExcel("report", **test_result)

    def test_orderPaymentDetailQuery(self):
        print("查询订单号"+globals()["order_no"])
        url = globalApiValueAndFunction.clientApiUrl + "/api/product/client/order/detail/" + globals()["order_no"]
        headers = {"conyent-type": "application/json;charset=UTF-8",
                   "X-Auth-Token": self.primaryUserClientToken}
        r = requests.get(url=url, headers=headers)
        print(r.content.decode('UTF-8'))
        result = json.loads(r.content)
        self.minimumUnpaidAmount = result['minimumUnpaidAmount']
        print(self.minimumUnpaidAmount)
        status_code = r.status_code
        if status_code == 200:
            test_result = {"0": "查询支付详情", "1": r.status_code, "2": "200", "3": status_code, "4": "通过",}
        else:
            test_result = {"0": "查询支付详情", "1": r.status_code, "2": "200", "3": status_code, "4": "不通过",}
        excelOperation.addDataToExistExcel("report", **test_result)
        self.assertIsNotNone(result['orderNo'])

        # gateway创建订单
        @unittest.skip("暂不执行")
        def test_createInstantOrderByGateway(self):
            url = globalApiValueAndFunction.clientApiUrl + "/api/product/client/order/from-api-gateway"
            headers = {"conyent-type": "application/json;charset=UTF-8",
                       "X-Auth-Token": self.primaryUserClientToken}
            data = {
                "blQuantity": 1,
                "includeInsurance": True,
                "couponsInfo": {
                    "couponId": "8aaa38d8735c4cb101735fd2aaca0003",
                    "amount": 1},
                "containerInfos": [
                    {
                        "containerType": "20GP",
                        "quantity": 1
                    },
                    {
                        "containerType": "40GP",
                        "quantity": 1
                    }
                ],
                "paymentChannel": "ONLINE",
                "productId": "8aaacf6872b745a30172b74ba0550003"
            }
            r = requests.post(url=url, json=data, headers=headers)

            result = json.loads(r.content)

if __name__ == '__main__':
    resultName = dateAndTimeFunction.automationResultTime()
    filename = 'D:\\workspace\\autotestPlatform\\data\\log\\apptestresult'+ resultName + '.html'
    suite = unittest.TestSuite()
    # suite.addTest(test_order("test_order_payment_detail_query"))
    suite.addTest(test_createInstantOrder("test_queryExtraFee"))
    suite.addTest(test_createInstantOrder("test_createInstantOrder"))
    # with(open('D:\\workspace\\autotestPlatform\\data\\log\\result.html', 'wb')) as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=fp,
    #         title='Seldom自动化测试报告',
    #         description='浏览器chrome,平台windows'
    #     )
    runner = unittest.TextTestRunner()
    runner.run(suite)