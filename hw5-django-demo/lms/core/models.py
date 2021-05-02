from django.db import models
from django.core.validators import RegexValidator
from lms.tasks import send_contact_us_email

class Group(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    teacher = models.ManyToManyField('core.Teacher')

    def __str__(self):
        return self.name


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+380123456789'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(default=14)

    def __str__(self):
        return self.fullname


class Teacher(models.Model):
    fullname = models.CharField(max_length=255)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+380123456789'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    def __str__(self):
        return self.fullname


class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name} - {self.email}"

    def save(self, *args, **kwargs):
        super(ContactUs, self).save(*args, **kwargs)
        send_contact_us_email.delay(self.name, self.message, self.email)


class Logger(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request_path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255)
    request_execution_time = models.FloatField()
