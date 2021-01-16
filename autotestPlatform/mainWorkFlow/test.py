#!usr/bin/python
# encoding:utf-8

import uuid
import time
import datetime
import codecs
import xlrd
import xlwt
from xlutils.copy import copy


class ect_api:
    def __init__(self):
        self

    def getWeekNo(self):
        firstDay = datetime.datetime(int(time.strftime("%Y")), 1, 1).strftime("%w")
        today = time.strftime("%w")
        week = time.strftime("%W")
        if int(firstDay) <= int(today) or today == 7 or today == 6:
            week = int(week) + 1
        weekNo = time.strftime("%Y") + str(week)
        return weekNo

    def getUUID(self):
        return "".join(str(uuid.uuid4()).split("-")).upper()

    def readAllTxt(self, path):
        with open(path, 'r') as f:
            content = f.read()
            return content

    def getCurrentTime(self):
        current = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return current

    def getYearMonthDay(self):
        YearMonthDay = datetime.datetime.now().strftime('%Y%m%d')
        return YearMonthDay

    def saveXml(self, fileName, content):
        with codecs.open('D:\\item-scripts\\BR\\' + fileName + '.xml', 'a+', encoding='utf-8') as f:
            f.write(content)

    def getCurrentTimeYMD(self):
        # current = datetime.datetime.utcnow().isoformat()
        day = datetime.datetime.now().strftime('%Y-%m-%d')
        return day

    # 创建一个保存结果的excel，并创建好第一行请求头
    def createAutomationResultsExcel(self, sheetName):
        resultName = self.getCurrentTimeYMD()
        # 新增一个excel来保存当日结果
        excel = xlwt.Workbook()
        # 先只新增一个sheet页面
        sheet = excel.add_sheet(sheetName)
        sheet.write(0, 0, "场景")
        sheet.write(0, 1, "用例")
        sheet.write(0, 2, "预期")
        sheet.write(0, 3, "实际")
        sheet.write(0, 4, "是否通过")
        excel.save('D:\\workspace\\autotestPlatform\\data\\report\\automationReport' + str(resultName) + '.xls')

    def addDataToExistExcel(self, sheetName, **kwargs):
        # 得用字典**kwargs
        # sheetName.在哪一个sheet添加数据，column在哪一列，value值
        resultName = self.getCurrentTimeYMD()
        excelDir = 'D:\\workspace\\autotestPlatform\\data\\report\\automationReport' + str(resultName) + '.xls'
        old_excel = xlrd.open_workbook(excelDir, formatting_info=True)
        # total_rows = excel.sheets()[1].nrows
        total_rows = old_excel.sheet_by_name(sheetName).nrows
        new_excel = copy(old_excel)
        print(total_rows)
        new_sheet = new_excel.get_sheet(sheetName)
        for col, value in kwargs.items():
            new_sheet.write(total_rows, int(col), value)
        new_excel.save(excelDir)

# if __name__ == '__main__':
#    print(ect_api().createAutomationResultsExcel("report"))

