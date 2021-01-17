import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from testcase.models import *
from django.shortcuts import render
from django.contrib import auth
import requests

# Create your views here.

def test(request):
    test1 = Case(name='runoob1',remark='runoob2',function='runoob3')
    test1.save()
    return HttpResponse(test1)

def testcase(request):
    context = {"runoob1":"ss"}
    test1 = Case.objects.all()
    return render(request, 'testcase.html', {"testcase_list":test1})

def login(request):
    return render(request, 'login.html')

def login_action(request):
    u_name = request.GET['username']
    u_pwd = request.GET['password']

    user = auth.authenticate(username=u_name,password=u_pwd)
    if user is not None:
        auth.login(request,user)
        request.session['user'] = u_name
        return HttpResponse('200')
    else:
        return HttpResponse("用户不存在")

def register_action(request):
    u_name = request.GET['username']
    u_pwd = request.GET['password']
    try:
        user = User.objects.create_user(username=u_name,password=u_pwd)
        user.save()
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册不成功")

@login_required
def welcome(request):
    return render(request, 'welcome.html')

#返回子页面
def child(request,eid,oid):
    resp = child_json(eid,oid)
    return render(request,eid,resp)

#控制不同的页面返回不同的数据，数据分发器
def child_json(eid,oid=''):
    res = {}
    if eid == 'home.html':
        date = DB_home_href.objects.all()
        res = {"hrefs":date}
    if eid == 'project_list.html':
        data = DB_project.objects.all()
        res = {"projects":data}
    if eid == 'P_apis.html':
        project = DB_project.objects.filter(id = oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {"project": project,"apis":apis}
    if eid == 'P_cases.html':
        project = DB_project.objects.filter(id = oid)[0]
        res = {"project": project}
    if eid == 'P_project_set.html':
        project = DB_project.objects.filter(id = oid)[0]
        res = {"project": project}
    return res

@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})

def register(request):
    return render(request, 'register.html')

#退出登录
def logout(request):
    auth.logout(request)
    return redirect('/login')

#吐槽
def pei(request):
    tucao_text = request.GET['tucao_text']
    return HttpResponse(DB_tucao.objects.create(username=request.user.username,remark=tucao_text))

#帮助
def api_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})

# 项目列表页面
def project_list(request):
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})

#  删除项目列表记录
def delete_project(request):
    project_id = request.GET['id']
    DB_project.objects.filter(id=project_id).delete()
    DB_apis.objects.filter(project_id=id).delete()
    return HttpResponse('删除成功')

# 新增项目记录
def add_project(request):
    project_name = request.GET['project_name']
    print(project_name)
    DB_project.objects.create(name=project_name,remark='',user=request.user.username,other_user='')
    return HttpResponse('保存成功')

#进入接口库页
def open_apis(request,id):
    project_id = id
    return render(request,'welcome.html',{"whichHTML":"P_apis.html","oid":project_id})

#  进入用例设置页
def open_cases(request,id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_cases.html", "oid": project_id})

#  进入用例设置页
def open_project_set(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_project_set.html", "oid": project_id})

#  新增接口
def project_api_add(request,Pid):
    project_id = Pid
    DB_apis.objects.create(project_id=project_id,api_method='none')
    return HttpResponseRedirect('/apis/%s' %project_id)

# 删除接口
def project_api_del(request,id):
    project_id = DB_apis.objects.filter(id=id)[0].project_id
    DB_apis.objects.filter(id=id).delete()
    return HttpResponseRedirect('/apis/%s' %project_id)

#新增接口备注
def save_bz(request):
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse('')

#获取接口备注
def get_bz(request):
    api_id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)

#保存接口具体内容
def Api_save(request):
    api_id = request.GET['api_id']
    api_name = request.GET['api_name']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']

    if ts_body_method == '返回体':
        api = DB_apis.objects.filter(id=api_id)[0]
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body
    else:
        ts_api_body = request.GET['ts_api_body']

    # 保存数据
    DB_apis.objects.filter(id=api_id).update(
        api_method=ts_method,
        api_url=ts_url,
        api_header=ts_header,
        api_host=ts_host,
        body_method=ts_body_method,
        api_body=ts_api_body,
        name=api_name
    )
    # 返回
    return HttpResponse('success')

#获取接口具体内容
def get_api_data(request):
    api_id = request.GET['api_id']
    api = DB_apis.objects.filter(id=api_id).values()[0]
    return HttpResponse(json.dumps(api),content_type='application/json')

#调试层发送请求
def Api_send(request):
    api_id = request.GET['api_id']
    api_name = request.GET['api_name']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['api_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']

    if ts_body_method == '返回体':
        api = DB_apis.objects.filter(id=api_id)[0]
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body

        if ts_body_method in ['',None]:
            return HttpResponse('请先设置好请求体编码格式和请求体，再点击Send按钮发送请求')
    else:
        ts_api_body = request.GET['ts_api_body']
        api = DB_apis.objects.filter(id=api_id)
        api.update(last_body_method=ts_body_method,last_api_body=ts_api_body)

    # 发送请求获取返回值
    try:
        header = json.loads(ts_header)  #处理header
    except:
        return HttpResponse('请求头不符合json格式！')
    print(header)
    #拼接完整url
    if ts_host[-1] == '/' and ts_url[0] == '/':   #都有/
        url = ts_host[:-1] + ts_url
    elif ts_host[-1] != '/' and ts_url[0] != '/':  #都没有/
        url = ts_host+'/'+ts_url
    else:
        url = ts_host + ts_url
    try:
        if ts_body_method == 'none':
            response = requests.request(ts_body_method.upper(),url,headers=header,data={})
        elif ts_body_method == 'form-data':
            files = []
            payload = {}
            for i in eval(ts_api_body):
                payload[i[0]] = i[1]
            response = requests.request(ts_body_method.upper(),url,headers=header,data=payload,files=files)
        elif ts_body_method == 'x-www-form-urlencoded':
            header['Content-Type'] = 'application/x-www-form-urlencoded'
            payload = {}
            for i in eval(ts_api_body):
                payload[i[0]] = i[1]
                response = requests.request(ts_body_method.upper(), url, headers=header, data=payload)
        else:   #这是raw的五个子选项
            if ts_body_method == 'Text':
                header['Content-Type'] = 'text/plain'
            if ts_body_method == 'Text':
                header['Content-Type'] = 'text/plain'
            if ts_body_method == 'Text':
                header['Content-Type'] = 'text/plain'
            if ts_body_method == 'Text':
                header['Content-Type'] = 'text/plain'
            if ts_body_method == 'Text':
                header['Content-Type'] = 'text/plain'
            response = requests.request(ts_body_method.upper(), url, headers=header, data=ts_api_body.encode('utf-8'))
        response.encoding = "utf-8"
        return HttpResponse(response.text)
    except Exception as e:
        return HttpResponse(str(e))

# 复制接口
def copy_api(request):
    api_id = request.GET['api_id']
    old_api = DB_apis.objects.filter(id=api_id)[0]
    DB_apis.objects.create(project_id=old_api.project_id,
                           name=old_api.name+'副本',
                           api_method=old_api.api_method,
                           api_url=old_api.api_url,
                           api_header=old_api.api_header,
                           api_login=old_api.api_login,
                           api_host=old_api.api_host,
                           des=old_api.des,
                           body_method=old_api.body_method,
                           api_body=old_api.api_body,
                           result=old_api.result,
                           sign=old_api.sign,
                           file_key=old_api.file_key,
                           file_name=old_api.file_name,
                           public_header=old_api.public_header,
                           last_body_method=old_api.last_body_method,
                           last_api_body=old_api.last_api_body
                           )
    return HttpResponse('')

#异常值发送请求
def error_request(request):
    api_id = request.GET['api_id']
    new_body = request.GET['new_body']
    span_text = request.GET['span_text']
    api = DB_apis.objects.filter(id=api_id)[0]
    method = api.api_method
    url = api.api_url
    host = api.api_host
    header = api.api_header
    body_method = api.body_method
    header = json.loads(header)
    if host[-1] == '/' and url[0] == '/':
        url = host[:-1] + url
    elif host[-1] != '/' and url != '/':
        url = host + '/'  + url
    else:
        url = host + url
    try:
        if body_method == 'form-data':
            files = []
            payload = {}
            for i in eval(new_body):
                payload[i[0]] = i[1]
            response = requests.request(method.upper(),url,headers=header,data=payload,files=files)
        elif body_method == 'x-www-form-urlencoded':
            header['Content-Type'] = 'application/x-www-form-urlencoded'
            payload = {}
            for i in eval(new_body):
                payload[i[0]] = i[1]
            response = requests.request(method.upper(), url, headers=header, data=payload)
        elif body_method == 'Json':
            header['Content-Type'] = 'text/plain'
            response = requests.request(method.upper(), url, headers=header, data=new_body.encode('utf-8'))
        else:
            return HttpResponse('非法的请求体类型')
        response.encoding = "utf-8"
        res_json = {"response":response.text,"span_text":span_text}
        return HttpResponse(json.dumps(res_json),content_type='application/json')
    except:
        res_json = {"response": '对不起，接口未通!', "span_text": span_text}
        return HttpResponse(json.dumps(res_json),content_type='application/json')


#返回echarts页面
def bar_chart(request):
    return render(request, 'bar_chart.html')
#返回自动化结果数据
def bar_chart_data(request):
    runDate_in =request.GET #获取前端传过来的数据
    runDate_string = runDate_in.get('runDate')
    print(runDate_in.get('runDate'))
    record_obj = []  #将sql查询结果转成数组
    result_obj = autotest_result.objects.filter(runDate=runDate_string)
    for re in result_obj :
        record = []
        record.append(re.runDate)
        record.append(re.module_name)
        record.append(re.pass_count)
        record.append(re.failed_count)
        record_obj.append(record)
    return HttpResponse(json.dumps(record_obj))

#返回运行日期
def getRunDate(request):
    runDate_obj = []
    runDates = autotest_result.objects.values('runDate').distinct()
    for date in runDates:
        runDate_obj.append(date)
    return HttpResponse(json.dumps(runDate_obj))

