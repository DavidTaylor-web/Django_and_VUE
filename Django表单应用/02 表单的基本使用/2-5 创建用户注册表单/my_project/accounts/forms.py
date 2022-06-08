from django import forms


class LoginForm(forms.Form):
    """ 登录表单 """
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=False,
                               help_text='使用帮助',
                               initial='admin')


class UserEditForm(forms.Form):
    """ 用户的信息维护 """
    SEX_CHOICES = (
        (1, '男生'),
        (0, '女生'),
    )
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=False,
                               help_text='使用帮助',
                               initial='admin')
    email = forms.EmailField(label='电子邮箱', max_length=200)
    age = forms.IntegerField(label='年龄')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    birth_date = forms.DateField(label='生日')
    avatar = forms.ImageField(label='用户头像')


class UserRegForm(forms.Form):
    """ 用户注册表单 """
    username = forms.EmailField(label='用户名', max_length=200, min_length=5)
    password = forms.CharField(label='密码', max_length=200, min_length=6)
    nickname = forms.CharField(label='用户昵称', max_length=32, required=False)
    birth_date = forms.DateField(label='用户的生日', required=False)