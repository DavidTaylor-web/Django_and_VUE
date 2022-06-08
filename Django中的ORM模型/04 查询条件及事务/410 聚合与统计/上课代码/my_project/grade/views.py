from django.db.models import Sum
from django.shortcuts import render

from grade.models import Grade, Student


def page_grade(request):
    """ 学生成绩的统计 """
    # 练习1：求某个学生期末成绩的总和
    grade_list = Grade.objects.filter(student_name='张三')
    total = grade_list.aggregate(total_score=Sum('score'))
    print(total)
    # 练习4：求每个学生期末成绩的总和
    stu_list = Student.objects.annotate(total=Sum('stu_grade__score'))

    return render(request, 'page_grade.html', {
        'total': total,
        'stu_list': stu_list
    })