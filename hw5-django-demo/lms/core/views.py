from django.views.generic.list import ListView
from core.models import Group, Teacher, Student
from django.db.models import F
from django.db.models.aggregates import Avg, Count, Max, Min


class IndexView(ListView):
    template_name = "group_detail.html"

    def get_queryset(self):
        return Group.objects.get_queryset(
        ).annotate(
            teacher_name=F('teacher__fullname'),
            student_count=Count('student'),
            student_avg_age=Avg('student__age'),
            student_max_age=Max('student__age'),
            student_min_age=Min('student__age'),
        )


class GroupView(ListView):
    template_name = "group.html"
    model = Group


class TeacherView(ListView):
    template_name = "teacher.html"
    model = Teacher


class StudentView(ListView):
    template_name = "student.html"
    model = Student
