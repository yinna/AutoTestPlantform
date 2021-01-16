import time,os,random,traceback
import unittest
from selenium import webdriver

from mainWorkFlow import commonUIFunction,dateAndTimeFunction

class test_clientFileUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.failureException = self.failure_monitor()
        commonUIFunction.clientLogin(self.driver,commonUIFunction.clientUrl,commonUIFunction.primaryUsername,commonUIFunction.clientPassword)

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

    #线下充值
    def test_offlineRecharge(self):
        driver = self.driver
        current = dateAndTimeFunction.currentTimeYMdHMS()   #获取当前时间年月日时分秒
        currentFormat = dateAndTimeFunction.currentTimeY_M_dHMS()
        driver.find_element_by_xpath("//a[@href='/user']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@href='/user/assets/recharge']").click()  #点击账户充值
        time.sleep(2)
        driver.find_element_by_xpath("//div[text()='请选择充值账户']/following-sibling::div[2]/label[2]/span").click()  #点击线下充值
        time.sleep(2)
        driver.find_element_by_xpath("//label[@for='serialNo']/following-sibling::div/div/input").send_keys(current)  #输入银行转账流水号/水单号
        driver.find_element_by_xpath("//label[@for='amount']/following-sibling::div/div/input").send_keys(int(2000))  # 输入充值金额
        driver.find_element_by_xpath("//label[@for='payBank']/following-sibling::div/div/input").send_keys("自动化测试银行")  # 输入付款银行
        driver.find_element_by_xpath("//label[@for='payAccount']/following-sibling::div/div/input").send_keys("autotest")  # 输入付款账户
        driver.find_element_by_xpath("//label[@for='rechargeTime']/following-sibling::div/div/input").send_keys(currentFormat)  # 输入转账日期
        driver.find_element_by_xpath("//label[@for='remark']/following-sibling::div/div/input").send_keys("UI自动化测试"+current)  # 输入录入备注
        driver.find_element_by_xpath("//span[text()=' 上传水单 ']").click()  #点击上传水单按钮
        time.sleep(1)
        os.system("D:\\workspace\\autotestPlatform\\data\\testData\\waterListUpload.exe")
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='确 定']").click()  #点击确定按钮，上传
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[@class='el-button el-button--default el-button--small el-button--primary ']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[text()='资产信息']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[text()='充值记录']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[text()='线下充值记录']").click()
        time.sleep(1)
        remark =driver.find_element_by_xpath("//div[@aria-labelledby='tab-offline']//tbody/tr[1]/td[10]/div[text()='UI自动化测试"+current+"']").text
        self.assertEqual(remark,"UI自动化测试"+current,"线下充值不成功")

    def tearDown(self):
        driver = self.driver
        commonUIFunction.closeBrowser(driver)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_clientFileUpload("test_offlineRecharge"))
    runner = unittest.TextTestRunner()
    runner.run(suite)