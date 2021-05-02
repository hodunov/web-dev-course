from django.contrib import admin
from .models import Student, Group, Teacher, ContactUs, Logger


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(ContactUs)
admin.site.register(Logger)
