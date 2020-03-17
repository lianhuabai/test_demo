from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from  django.contrib.auth.decorators import login_required
# Create your views here.
def say_hello(request):
    name = request.GET.get("name","")
    if name == "":
        return HttpResponse("请输入名称")
    return render(request,"index.html",{"name":name})

def index(request):
    '''
    登录首页
    '''
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码输入为空"})
        user = auth.authenticate(username=username,password=password)
        print("user--------",user)
        if user is None:
            return render(request,"index.html",{"error":"用户名或者密码错误"})
        else:
            auth.login(request,user)#记录用户登录状态
            return  HttpResponseRedirect("/project/")#登录成功重定向

#登录成功项目管理页面
@login_required()
def project(request):
    return render(request, "project.html")

#模块管理
@login_required()
def modeul(request):
    return render(request, "modeul.html")

#退出登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")