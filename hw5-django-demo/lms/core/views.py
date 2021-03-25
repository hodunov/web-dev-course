from django.views.generic.list import ListView
from core.models import Group, Teacher, Student


class GroupView(ListView):
    template_name = "group.html"
    model = Group

class TeacherView(ListView):
    template_name = "teacher.html"
    model = Teacher

class StudentView(ListView):
    template_name = "student.html"
    model = Student