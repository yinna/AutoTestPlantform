from django.db import models

# Create your models here.

class Case(models.Model):
    name = models.CharField(max_length=20)  #case的名称
    remark = models.CharField(max_length=20)  #描述
    function = models.CharField(max_length=20)
    def __str__(self):
        return self.name+self.remark+self.function

class DB_tucao(models.Model):
    username = models.CharField(max_length=30,null=True)  #吐槽人的名称
    remark = models.CharField(max_length=1000,null=True)  #吐槽内容
    create_time = models.DateTimeField(auto_now=True)  #吐槽时间
    def __str__(self):
        return self.username+self.remark+str(self.create_time)

class DB_home_href(models.Model):
    name = models.CharField(max_length=30,null=True)  #超链接名字
    href = models.CharField(max_length=2000,null=True)  #超链接内容
    def __str__(self):
        return self.name+self.href

# 项目列表
class DB_project(models.Model):
    name = models.CharField(max_length=100,null=True)  #项目名字
    remark = models.CharField(max_length=1000,null=True)  #项目备注
    user = models.CharField(max_length=15,null=True)  #项目创建者名字
    other_user = models.CharField(max_length=200,null=True)  #项目其他创建者
    create_time = models.DateTimeField(auto_now=True)  #项目创建时间
    def __str__(self):
        return self.name + self.user

#   接口表
class DB_apis(models.Model):
    project_id = models.CharField(max_length=10,null=True) #项目id
    name =  models.CharField(max_length=100,null=True) #接口名字
    api_method =  models.CharField(max_length=10,null=True) #请求方式
    api_url =  models.CharField(max_length=1000,null=True) #url
    api_header =  models.CharField(max_length=1000,null=True) #请求头
    api_login =  models.CharField(max_length=10,null=True) #是否带登陆态
    api_host =  models.CharField(max_length=100,null=True) #域名
    des =  models.CharField(max_length=100,null=True) #描述
    body_method =  models.CharField(max_length=25,null=True) #请求体编码格式
    api_body =  models.CharField(max_length=1000,null=True) #请求体
    result =  models.TextField(null=True) #返回体 因为长度巨大，所以用大文本方式存储
    sign =  models.CharField(max_length=10,null=True) #是否验签
    file_key =  models.CharField(max_length=50,null=True) #文件key
    file_name =  models.CharField(max_length=50,null=True) #文件名
    public_header =  models.CharField(max_length=1000,null=True) #全局变量-请求头

    last_body_method = models.CharField(max_length=25,null=True) #上一次请求体编码格式
    last_api_body = models.CharField(max_length=1000, null=True)  # 上一次请求体
    def __str__(self):
        if self.name:
            return self.name
        else:
            return "空"

# 自动化测试结果
class autotest_result(models.Model):
    runDate = models.CharField(max_length=256,null=True)  #脚本日期
    module_name = models.CharField(max_length=256,null=True)  #模块名称
    pass_count = models.IntegerField(null=True)  #成功数
    failed_count = models.IntegerField(null=True)  #失败数
    version = models.IntegerField(null=True)
    create_by = models.CharField(max_length=256, null=True)
    create_time = models.DateTimeField(auto_now=True)  #保存创建时间
    update_by = models.CharField(max_length=256, null=True)
    update_time = models.DateTimeField(auto_now=True)  # 保存更新时间
    def __str__(self):
        return self.runDate + self.module_name+str(self.pass_count)+str(self.failed_count)