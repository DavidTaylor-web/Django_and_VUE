from django.shortcuts import render


def page_grade(request):
    """ 学生成绩的统计 """
    return render(request, 'page_grade.html', {

    })