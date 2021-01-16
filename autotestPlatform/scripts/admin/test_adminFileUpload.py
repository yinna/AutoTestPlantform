import unittest
import time
import os,random,traceback
from mainWorkFlow import commonUIFunction, commonUIXpath
from mainWorkFlow import connectDatabase,dateAndTimeFunction
from selenium import webdriver

class test_adminFileUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.failureException = self.failure_monitor()
        commonUIFunction.adminLogin(self.driver,commonUIFunction.adminUrl,"China", commonUIFunction.adminUsername, commonUIFunction.adminPassword)

    def failure_monitor(self):
        test_case = self  # 将self赋值给test_case，以便下方的AssertionErrorPlus内部类可调用外部类的方法

        class AssertionErrorPlus(AssertionError):
            def __init__(self, msg):
                try:
                    cur_method = test_case._testMethodName  # 当前test函数的名称
                    unique_code = ''.join(random.sample('1234567890', 5))  # 随机生成一个值，以便区分同一个test函数内不同的截图
                    file_name = '%s_%s.png' % (cur_method, unique_code)
                    test_case.driver.get_screenshot_as_file(os.path.join("D:\\workspace\\autotestPlatform\\data\\log\\", file_name))  # 截图生成png文件
                    print('失败截图已保存到: %s' % file_name)
                    msg += '\n失败截图文件: %s' % file_name
                except BaseException:
                    print('截图失败: %s' % traceback.format_exc())

                super(AssertionErrorPlus, self).__init__(msg)

        return AssertionErrorPlus  # 返回AssertionErrorPlus类

    def test_couponsUpload(self):
        driver = self.driver
        commonUIXpath.clickFirstLevelMenu(driver,"特惠管理")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver,"优惠券管理")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='button']//span[text()='手工上载']").click()
        time.sleep(3)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\couponsUpload.exe")
        time.sleep(3)
        rows = connectDatabase.DBReturnRows("SELECT count(*) FROM COUPON c2 WHERE c2.COUPON_RULE_UUID='8aaade2a73b702f80173b87e13ca00cc' AND COMPANY_UUID ='8aaa614a6aaf570e016aafc997cc0001' AND CREATE_TIME > SYSDATE-1")
        self.assertEqual("2",rows,"桁架结构")

    def test_crossbookingInventoryUpload(self):
        driver = self.driver
        today = dateAndTimeFunction.currentTimeY_M_d()
        commonUIXpath.clickFirstLevelMenu(driver,"Cross Booking")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver,"库存维护")
        time.sleep(3)
        driver.find_element_by_xpath("//span[text()='上传']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='选取文件并上传']").click()
        time.sleep(1)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\crossbookingInventoryUpload.exe")
        time.sleep(3)
        rows = connectDatabase.DBReturnRows("select count(*) from cb_inv_operation where cb_inv_uuid = '8aaadf75759b894301759ca0558418bd' AND TO_CHAR(OPERATE_TIME,'yyyy-mm-dd') ='"+today+"'")
        self.assertEqual("1",rows,"上传库存模板历史记录加一行")

    def test_rateNunberUpload(self):
        driver = self.driver
        commonUIXpath.clickFirstLevelMenu(driver, "订单管理")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver, "订单查询")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='button']//span[text()='上载制约号']").click()
        time.sleep(3)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\rateNunberUpload.exe")
        time.sleep(1)
        tips = driver.find_element_by_xpath("//p[text()='上传成功']").text
        self.assertEqual("上传成功", tips, "上传制约号成功")

    @unittest.skip("暂不执行")
    def test_transshipmentFeeUpload(self):
        driver = self.driver
        commonUIXpath.clickFirstLevelMenu(driver, "基础数据维护")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver, "转运附加费")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver, "内陆转运费")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='button']//span[text()='内陆转运费excel上传']").click()
        time.sleep(3)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\transshipmentFeeUpload.exe")
        time.sleep(3)
        rows = connectDatabase.DBReturnRows("SELECT count(*) FROM TRANSSHIPMENT_CHARGE WHERE COMMODITY_CODE LIKE '自动化测试内陆转运费%'")
        self.assertEqual("2", rows, "上传内陆转运附加费行数是2")

    def tearDown(self):
        driver = self.driver
        commonUIFunction.closeBrowser(driver)

    @classmethod
    def tearDownClass(self):
        sql = ["DELETE FROM TRANSSHIPMENT_CHARGE_DETAIL tcd WHERE tcd.TRANSSHIPMENT_CHARGE_HIS_UUID IN (SELECT tch.UUID FROM TRANSSHIPMENT_CHARGE_HIS tch WHERE tch.TRANSSHIPMENT_CHARGE_UUID IN (SELECT tc.UUID FROM TRANSSHIPMENT_CHARGE tc WHERE tc.COMMODITY_CODE LIKE '自动化测试内陆转运费%'))","DELETE FROM TRANSSHIPMENT_CHARGE_HIS tch WHERE tch.TRANSSHIPMENT_CHARGE_UUID IN (SELECT tc.UUID FROM TRANSSHIPMENT_CHARGE tc WHERE tc.COMMODITY_CODE LIKE '自动化测试内陆转运费%')","DELETE FROM TRANSSHIPMENT_CHARGE tc WHERE tc.COMMODITY_CODE LIKE '自动化测试内陆转运费%'"]
        connectDatabase.multiExcuteSql(sql)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_adminFileUpload("test_transshipmentFeeUpload"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
