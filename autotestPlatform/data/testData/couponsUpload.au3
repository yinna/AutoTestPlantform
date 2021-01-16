; 等待5秒钟，让上传窗口出现
WinWait("[CLASS:#32770]","",5)

;把输入焦点定位到上传输入文本框中,类型为Edit,编号为1，也就是上面获取到内容
ControlFocus("Open", "","Edit1")  

;在文件名那里，输入需要上传的文件绝对路径
ControlSetText("Open", "", "Edit1", 'D:\workspace\autotestPlatform\data\testData\手工上载模板.xlsx')

;等待上传时间，单位是毫秒 1秒 = 1000 毫秒，文件大的话需要设置长点
Sleep(5000)

;点击"打开"按钮，也就是上传，完成整个上传过程
ControlClick("Open", "","Button1");