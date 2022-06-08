from django.urls import path

from accounts import views

urlpatterns = [
    # 用户登录表单
    path('user/login/', views.user_login, name='user_login'),
    # 用户详细信息
    path('user/info/', views.user_info, name='user_info'),
    # 用户退出登录
    path('user/logout/', views.user_logout, name='user_logout'),
]