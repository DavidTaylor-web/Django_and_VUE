from django.urls import path

from master import views

urlpatterns = [
    # echarts的使用
    path('test/', views.test, name='test'),
]