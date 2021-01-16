import HTMLTestRunner
import os

import xlrd
import unittest

from mainWorkFlow import excelOperation
from mainWorkFlow import sendEmail

Dir = "../scripts/"
def findScriptsAndImport(rootDir):
    # #遍历rootDir下所有目录，import所有test_*.py
    list_dirs = os.walk(rootDir)
    for dirName,subdirList,fileList in list_dirs:
        print("目录名称"+dirName+"--")
        for f in fileList:
            fileName = f
            if fileName[0:5] == "test_" and fileName[-3:] == ".py":
                if dirName[-1:] != "/":
                    impPath = dirName.replace("/",".")[3:].replace("\\",".")
                else:
                    impPath = dirName.replace("/",".")[3,-1]
                if impPath != "":
                    exe_str = "from " + impPath + " import " + fileName[0:-3]
                    print("不等于空"+exe_str)
                else:
                    exe_str = "import" + fileName[0,-3]
                    print(exe_str)
                exec (exe_str,globals())
    '''
    获取TestCases下所有的测试用例
    :param pattern: 匹配模式
    :return: 测试用例集
    '''
    # discover_all_cases=unittest.defaultTestLoader.discover("D:\\workspace\\autotestPlatform\\scripts",pattern="test*.py",top_level_dir=None)   #testcase_path是测试用例的根目录
    # return discover_all_cases

def get_xls_case_by_index(sheet_name):
    """获取excel表中指定的sheet数据，保存到列表中返回"""
    xls_path = "D:\\workspace\\autotestPlatform\\data\\各环境基础测试数据.xls"
    file = xlrd.open_workbook(xls_path)
    sheet = file.sheet_by_name(sheet_name)
    ncols = sheet.ncols
    for j in range(ncols):
        cell_value = sheet.cell_value(0,j)
        if cell_value == "fileName":
            col1 = j
        if cell_value == "className":
            col2 = j
        if cell_value == "caseName":
            col3 = j
    nrows = sheet.nrows
    caseList = []
    for i in range(1,nrows):
        if sheet.row_values(i)[0].lower().strip() == "ready":
            fileName = sheet.cell_value(i,col1)
            className = sheet.cell_value(i,col2)
            caseName = sheet.cell_value(i,col3)
            case = '%s.%s("%s")' % (fileName.strip(),className.strip(),caseName.strip())
            caseList.append(case)
            print("测试用例"+case)
    return caseList


if __name__ == '__main__':
    findScriptsAndImport(Dir)
    excelOperation.createAutomationResultsExcel("report")  #创建一个保存断言结果的excel
    suite = unittest.TestSuite()
    for testcase in get_xls_case_by_index("脚本执行顺序"):
        suite.addTest(eval(testcase))
        print(testcase)
    with(open('D:\\workspace\\autotestPlatform\\data\\log\\result.html', 'wb')) as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Seldom自动化测试报告',
            description='浏览器chrome,平台windows'
        )
        runner.run(suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #to do将结果保存到excel里，已经每个测试用例自己保存好了
    # 发送邮件
    # sendEmail.sendAutotestResult()
