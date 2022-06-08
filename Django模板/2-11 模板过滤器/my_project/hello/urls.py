from django.urls import path

from hello.views import index, tag, test_filter

urlpatterns = [
    path('index/', index, name='index'),
    path('tag/', tag, name='tag'),
    path('test/filter/', test_filter, name='test_filter'),
]