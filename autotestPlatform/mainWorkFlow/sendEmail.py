#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#发送测试报告
def sendAutotestResult():
    sender = '532066995@qq.com'
    receivers = ['jane.yin@oocl.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("自动化回归测试", 'utf-8')
    message['To'] = Header("自动化回归测试", 'utf-8')
    subject = '自动化回归测试结果'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是回归测试结果', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 automationReport20201015.xls 文件
    att1 = MIMEText(open('D:\\workspace\\autotestPlatform\\data\\report\\automationReport20201018.xls', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "自动化回归测试结果.xls"))
    # att1["Content-Disposition"] = 'result'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP('smtpapp1.oocl.com')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    sendAutotestResult()