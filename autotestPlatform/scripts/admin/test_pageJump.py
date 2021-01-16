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

    def test_product(self):
        driver = self.driver
        commonUIXpath.clickFirstLevelMenu(driver,"航线产品")
        time.sleep(1)
        commonUIXpath.clickSecondLevelMenu(driver,"航线产品管理")
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(3)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\couponsUpload.exe")
        time.sleep(3)
        rows = connectDatabase.DBReturnRows("SELECT count(*) FROM COUPON c2 WHERE c2.COUPON_RULE_UUID='8aaade2a73b702f80173b87e13ca00cc' AND COMPANY_UUID ='8aaa614a6aaf570e016aafc997cc0001' AND CREATE_TIME > SYSDATE-1")
        self.assertEqual("2",rows,"桁架结构")

    def tearDown(self):
        driver = self.driver
        commonUIFunction.closeBrowser(driver)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_adminFileUpload("test_rateNunberUpload"))
    runner = unittest.TextTestRunner()
    runner.run(suite)