from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from accounts.models import User, UserProfile


def query_course(request):
    c = request.GET.get('c', None)
    query = Q()
    if c is not None:
        query = query & Q()
    sort = request.GET.get('sort', None)
    if sort is not None:
        query = query & Q()


def user_info(request):
    """ 用户详情-查询优化 """
    user = User.objects.get(pk=1)
    # profile_list = UserProfile.objects.all()
    profile_list = UserProfile.objects.all().select_related('user')

    # 使用SQL查询
    user_list = User.objects.raw('SELECT * FROM  `accounts_user`')
    return render(request, 'user_info.html', {
        'user': user,
        'profile_list': profile_list,
        'user_list': user_list
    })


def user_list_slice(request):
    """ 分页-使用切片 """
    page = request.GET.get('page', 1)
    return render(request, 'user_list_slice.html', {
    })


def user_list_paginator(request):
    """ 分页-使用分页器 """
    page = request.GET.get('page', 1)

    return render(request, 'user_list_paginator.html', {
    })