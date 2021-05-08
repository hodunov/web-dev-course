import csv
import datetime
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy

from core.models import Group, Teacher, Student, ContactUs
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


class ContactUsView(CreateView):
    template_name = "contact_us.html"
    success_url = reverse_lazy("contact_done")
    model = ContactUs
    fields = "__all__"


def export_students_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition':
                f'attachment; '
                f'filename=f"students-{datetime.datetime.now()}.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow([
        'Full name', 'Group', 'Birthday',
        'Phone', 'Email', 'Gender', 'Age',
    ])

    students = Student.objects.all()
    for student in students:
        writer.writerow([
            student.fullname, student.group, student.birthday,
            student.phone_number, student.email, student.gender,
            student.age,
        ])
    return response
