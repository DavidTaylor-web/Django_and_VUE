from django.shortcuts import render
from django.urls import reverse


class Cat(object):

    def display(self):
        return '我是中华田园猫'


def index(request):
    username = '张三'
    age = 25
    img_url = '/media/images/dog.jpg'

    list_users = [
        {'name': '张三', 'age': 34},
        {'name': '李四', 'age': 23},
    ]
    user_obj = {
        'user name': '王五',
        'user.name': '万二麻子'
    }
    cat = Cat()
    return render(request, 'index.html', {
        'username': username,
        'age': age,
        'img_url': img_url,
        'list_users': list_users,
        'user_obj': user_obj,
        'cat': cat
    })


def tag(request):
    """ DTL的标签练习 """
    list_users = [
        {'name': '张三', 'age': 34},
        {'name': '李四', 'age': 23, 'sex': '男'},
        {'name': '张三2', 'age': 34},
        {'name': '李四2', 'age': 23},
    ]
    # list_users = []
    # reverse()
    return render(request, 'tag.html', {
        'list_users': list_users
    })
