from django.shortcuts import render

from accounts.forms import LoginForm


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单验证通过')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })


def user_info(request):
    """ 用户信息 """
    return render(request, 'user_info.html')
