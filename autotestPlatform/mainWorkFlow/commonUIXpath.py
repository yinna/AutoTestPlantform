
def clickFirstLevelMenu(driver,firstMenuName):
    driver.find_element_by_xpath("//span[text()='" + firstMenuName + "']").click()

def clickSecondLevelMenu(driver,secondMenuName):
    driver.find_element_by_xpath("//span[text()='" + secondMenuName + "']").click()

