from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def hello_china(request):
    return HttpResponse('hello china')


def hello_html(request):
    """ 响应HTML内容 """
    username = '张三'
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello {{html}}</h1>
        </body>
    </html>
    """.replace('{{html}}', username)
    return HttpResponse(html)
