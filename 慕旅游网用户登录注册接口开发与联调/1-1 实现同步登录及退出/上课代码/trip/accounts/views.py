from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import LoginForm


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.do_login(request)
            print('表单验证通过')
            return redirect('/accounts/user/info/')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })


# @login_required(login_url='/accounts/user/login/')
@login_required
def user_info(request):
    """ 用户信息 """
    print(request.user)
    return render(request, 'user_info.html')


def user_logout(request):
    """ 用户退出登录 """
    logout(request)
    return redirect('/accounts/user/info/')