import datetime

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


def test_filter(request):
    """ 过滤器的使用 """
    name = 'model'
    # list_user = []
    list_user = False
    user_info = None
    pi = 3.1415926
    my_date = datetime.datetime(2050, 9, 28)
    html = '<h3>欢迎学习我们的python课程，祝大家学习愉快</h3>'
    return render(request, 'test_filter.html', {
        'name': name,
        'list_user': list_user,
        'user_info': user_info,
        'pi': pi,
        'my_date': my_date,
        'html': html
    })


def mine_filter(request):
    """ 自定义过滤器 """
    uname = '张三的昵称'
    return render(request, 'mine_filter.html', {
        'uname': uname
    })