from django.db import models
from django.core.validators import RegexValidator


class Group(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+380991234567'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.fullname
