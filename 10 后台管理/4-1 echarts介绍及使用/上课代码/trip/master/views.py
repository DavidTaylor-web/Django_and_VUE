from django.shortcuts import render

def test(request):
    """  echarts的使用 """
    return render(request, 'master/test.html')
