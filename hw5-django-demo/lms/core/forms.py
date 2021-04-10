from django import forms
from core.models import Student, Group, Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

