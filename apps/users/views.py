from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm
from .models import UserProfile

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
            else:
                return render(request, 'login.html', {
                    'loginform': loginform,
                    'message': '用户名或密码错误，请重新输入！'
                })
        return render(request, 'login.html', {
            'loginform': loginform,
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('learning_logs:index'))


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'register.html', {
                    'register_form': register_form,
                    'msg': '该用户名已存在，请重新输入',
                })
            user = UserProfile()
            user.username = user_name
            user.password = make_password(request.POST.get('password', ''))
            user.save()
            return render(request, 'index.html', {})
        else:
            return render(request, 'register.html', {
                'register_form': register_form,
            })