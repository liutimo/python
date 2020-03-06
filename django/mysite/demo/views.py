from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        return render(request, 'login.html')
    return render(request, 'register.html', {'error_msg': '注册失败'})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print('%s : %s' % (username, password))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                return HttpResponse("用户已激活")
            else:
                return HttpResponse("用户未激活")
        else:
            return render(request, 'login.html', {'error_msg': '用户名密码错误'})
    else:
        return render(request, 'login.html', {'error_msg': '用户名密码错误'})
