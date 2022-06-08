from django.urls import path

from hello.views import index, tag, test_filter, mine_filter

urlpatterns = [
    path('index/', index, name='index'),
    path('tag/', tag, name='tag'),
    path('test/filter/', test_filter, name='test_filter'),
    path('mine/filter/', mine_filter, name='mine_filter'),
]