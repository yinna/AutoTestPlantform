import xlrd
import xlwt
from mainWorkFlow import dateAndTimeFunction
from xlutils.copy import copy

global filePath
filePath = 'D:\\workspace\\autotestPlatform\\data\\report\\automationReport'
def readTestData(sheetName,row,column):
    # 1读取Excel测试用例
    excelDir = r'D:\\workspace\\autotestPlatform\\data\\各环境基础测试数据.xls'
    # 1-1打开excel文件
    workbook = xlrd.open_workbook(excelDir, formatting_info=True)
    # 1-2通过表单名获取表单
    workSheet = workbook.sheet_by_name(sheetName)
    # 1-3读取指定单元格
    return workSheet.cell(row, column).value

# 创建一个保存结果的excel，并创建好第一行请求头
def createAutomationResultsExcel(sheetName):
    resultName = dateAndTimeFunction.automationResultTime()
    # 新增一个excel来保存当日结果
    excel = xlwt.Workbook()
    # 先只新增一个sheet页面
    sheet = excel.add_sheet(sheetName)
    sheet.write(0, 0, "场景")
    sheet.write(0, 1, "用例")
    sheet.write(0, 2, "预期")
    sheet.write(0, 3, "实际")
    sheet.write(0, 4, "是否通过")
    excel.save(filePath + str(resultName) + '.xls')

def addDataToExistExcel(sheetName,**kwargs):
    # 得用字典**kwargs
    #sheetName.在哪一个sheet添加数据，column在哪一列，value值
    resultName = dateAndTimeFunction.automationResultTime()
    excelDir = filePath + str(resultName) + '.xls'
    old_excel = xlrd.open_workbook(excelDir, formatting_info=True)
    #total_rows = excel.sheets()[1].nrows
    total_rows = old_excel.sheet_by_name(sheetName).nrows
    new_excel = copy(old_excel)
    print(total_rows)
    new_sheet = new_excel.get_sheet(sheetName)
    for col,value in kwargs.items():
        new_sheet.write(total_rows, int(col), value)
    new_excel.save(excelDir)

# if __name__ == '__main__':
#     dicta = {"0": 'Test', "1": "24", "2": 'test@qq.com'}
#     addDataToExistExcel("Sheet1",**dicta)