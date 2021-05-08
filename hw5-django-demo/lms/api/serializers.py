from rest_framework import serializers

from core.models import Group, Student, Teacher


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'created', 'updated', 'description', 'teacher']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['fullname', 'group', 'phone_number', 'email', 'gender', 'age']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['fullname', 'birthday', 'phone_number', 'email', 'gender']



