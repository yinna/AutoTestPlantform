from selenium import webdriver
import time

global driver,adminUsername,adminPassword,adminUrl,clientUrl,primaryUsername,clientPassword


adminUsername = "seven.shen"
adminPassword = "Change_name22"
adminUrl = "http://admin.ectpp.opsmart.cn/login"
clientUrl = "http://mall.ectpp.opsmart.cn/"
primaryUsername = "janetest"
clientPassword = "Ect2020!!"

def adminLogin(driver,url,tenant,username,password):
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@role='button']").click()  # 转换成中文
    time.sleep(1)
    driver.find_element_by_xpath("//li[text()='中文']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@placeholder='域账号名']").send_keys(username)
    time.sleep(0.7)
    driver.find_element_by_xpath("//input[@placeholder='域账号密码']").send_keys(password)
    time.sleep(0.7)
    driver.find_element_by_xpath("//button").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='"+tenant+"']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确认']").click()
    time.sleep(3.5)

def clientLogin(driver,url,username,password):
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='Allow All']").click()  #同意GDPR条款
    time.sleep(1)
    driver.find_element_by_xpath("//b[text()='ENG']").click()  # 转换成中文
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='中文']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[text()='登录/注册']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='login_dialog_username']").send_keys(username)
    time.sleep(0.7)
    driver.find_element_by_xpath("//input[@id='login-password-input']").send_keys(password)
    time.sleep(0.7)
    driver.find_element_by_xpath("//span[text()='登录']").click()
    time.sleep(3)

def closeBrowser(driver):
    driver.close()
    driver.quit()

# if __name__ == '__main__':
    # clientLogin(primaryUsername,clientPassword)
    # closeBrowser()