from django.db.models import Q
from django.shortcuts import render

# Create your views here.

def query_course(request):
    c = request.GET.get('c', None)
    query = Q()
    if c is not None:
        query = query & Q()
    sort = request.GET.get('sort', None)
    if sort is not None:
        query = query & Q()

