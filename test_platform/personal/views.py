from django.shortcuts import render
from  django.http import HttpResponse
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
        print(username)
        print(password)
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码输入为空"})
        elif username != "ygc" or password != "930105":
            return render(request, "index.html", {"error": "用户名或密码错误"})
        elif username == "ygc" and password == "930105":
            return HttpResponse("登录成功")