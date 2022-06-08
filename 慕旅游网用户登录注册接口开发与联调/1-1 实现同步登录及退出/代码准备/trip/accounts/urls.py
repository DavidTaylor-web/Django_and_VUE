from django.urls import path

from accounts import views

urlpatterns = [
    # 用户登录表单
    path('user/login/', views.user_login, name='user_login'),
    path('user/info/', views.user_info, name='user_info'),
]