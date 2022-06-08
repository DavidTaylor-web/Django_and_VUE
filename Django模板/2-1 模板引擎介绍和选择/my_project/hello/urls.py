from django.urls import path

from hello.views import hello_html

urlpatterns = [
    path('html/', hello_html, name='html'),
]