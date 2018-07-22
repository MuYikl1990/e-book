from django.shortcuts import render, get_object_or_404, reverse
import re
from .models import Passport
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
def register(request):
    return render(request, 'users/register.html')

def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    if  not all([username, password, email]):
        context = {'errormsg': '参数不能为空! '}
        return render(request, 'users/register.html', context)

    if not re.match(r'^[A-Za-z0-9][\w\.\-]*@[a-z0-9]+(\.[a-z]{2,5}){1,2}$', email):
        context = {'errormsg': '邮箱不合法! '}
        render(request, 'users/register.html', context)

    try:
        Passport.objects.add_one_passport(username=username, password=password, email=email)
    except:
        context = {'errormsg': '用户名已存在! '}
        render(request, 'users/register.html', context)

    return HttpResponseRedirect(reverse('books:index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('books:index'))

