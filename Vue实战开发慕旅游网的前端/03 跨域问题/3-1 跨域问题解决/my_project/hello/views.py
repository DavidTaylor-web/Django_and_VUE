from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def world(request):
    return JsonResponse({
        'name': '张三',
        'age': 21
    })
