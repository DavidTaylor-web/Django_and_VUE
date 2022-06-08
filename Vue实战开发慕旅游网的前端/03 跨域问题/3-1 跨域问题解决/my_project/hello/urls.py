from django.urls import path

from hello.views import index, world

urlpatterns = [
    path('index/', index, name='index'),
    path('world/', world, name='world'),
]