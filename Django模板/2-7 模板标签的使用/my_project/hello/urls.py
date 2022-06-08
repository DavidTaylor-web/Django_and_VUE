from django.urls import path

from hello.views import index, tag

urlpatterns = [
    path('index/', index, name='index'),
    path('tag/', tag, name='tag'),
]