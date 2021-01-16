"""AutoFile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from testcase.views_group import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('testcase/', views.testcase),
    path('login/', views.login),  #open login page
    path('login_action/', views.login_action),  #excute login
    path('register_action/', views.register_action),
    path('welcome/', views.welcome),
    path('home/', views.home),
    path('register/', views.register),
    path('accounts/login/', views.login),
    path('logout/', views.logout),
    path('pei/', views.pei),  #吐槽
    path('help/', views.api_help),  #帮助
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", views.child),
    url(r"^project_list/$", views.project_list),
    path('delete_project/', views.delete_project),  #删除项目记录
    path('add_project/', views.add_project),   #新增项目记录
    url(r"^apis/(?P<id>.*)/$", views.open_apis),   #进入接口库
    url(r"^cases/(?P<id>.*)/$", views.open_cases),   #进入用例设置
    url(r"^project_set/(?P<id>.*)/$", views.open_project_set),   #进入项目设置
    url(r"^project_api_add/(?P<Pid>.*)/$", views.project_api_add),   #新增接口
    url(r"^project_api_del/(?P<id>.*)/$", views.project_api_del),   #删除接口
    url(r"^save_bz/$",views.save_bz),   #保存接口备注
    url(r"get_biz/$",views.get_bz),  #获取备注
    url(r"Api_save/$",views.Api_save),  #保存接口
    url(r"get_api_data/$",views.get_api_data),  #获取接口数据
    url(r"Api_send/$",views.Api_send),  #调试层发送请求
    url(r"copy_api/$",views.copy_api),  # 复制接口
    url(r"error_request/$",views.error_request),  # 调用异常测试接口

    path('chart/bar/', views.bar_chart),  #柱状图
    path('echarts_bar/data/', views.bar_chart_data),  #运行结果
    path('echarts_bar/getRunDate/', views.getRunDate),  #获取运行日期
]
