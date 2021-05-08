from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker  # https://model-bakery.readthedocs.io/en/latest/basic_usage.html
from django.template.loader import render_to_string

from core.models import Group, Student, Teacher


class TestCoreModels(TestCase):
    """
    Class to test models: Group, Student, Teacher
    """

    def setUp(self):
        """Set up test class."""
        self.teacher = baker.make(Teacher, fullname="Philip Kindred Dick", email="philip@dick.com")
        self.group = baker.make(Group, make_m2m=True, name="Top Group")
        self.student = baker.make(Student, age=42, fullname="Stephen King")

    def test_teacher(self):
        """Test function Teacher using baked model."""
        self.assertIsInstance(self.teacher, Teacher)

    def test_student(self):
        """Test function Student using baked model."""
        self.assertIsInstance(self.student, Student)
        self.assertEqual(self.student.age, 42, msg="Should be equal 42")

    def test_group(self):
        """Test function Group using baked model."""
        self.assertIsInstance(self.group, Group)

    def test_teacher_str(self):
        """Test model Teacher string representation."""
        self.assertEqual(str(self.teacher), "Philip Kindred Dick")

    def test_student_str(self):
        """Test model Student string representation."""
        self.assertEqual(str(self.student), "Stephen King")

    def test_group_str(self):
        """Test model Group string representation."""
        self.assertEqual(str(self.group), "Top Group")


class TemplateTest(TestCase):
    """
    Class to test asserts that the template with the given name was used in rendering the response.
    """
    def test_index_template(self):
        """Test index.html template"""
        with self.assertTemplateUsed(template_name='index.html'):
            render_to_string('index.html')


class SimpleUlrTest(TestCase):
    """
    Class to test HTTP response
    """

    def test_group_url(self):
        client = Client()
        response = client.get('/group/')
        response_from_create = client.get('/group/create', follow=True)
        self.assertEqual(response.status_code, 200, msg="/group/ Bad response status code")
        self.assertEqual(response_from_create.status_code, 200, msg="/group/create Bad response status code")

    def test_teacher_url(self):
        client = Client()
        response = client.get('/teacher/')
        response_from_create = client.get('/teacher/create', follow=True)
        self.assertEqual(response.status_code, 200, msg="/teacher/create Bad response status code")
        self.assertEqual(response_from_create.status_code, 200, msg="/teacher/create Bad response status code")

    def test_student_url(self):
        client = Client()
        response = client.get('/student/')
        response_from_create = client.get('/student/create', follow=True)
        self.assertEqual(response.status_code, 200, msg="/student/ Bad response status code")
        self.assertEqual(response_from_create.status_code, 200, msg="/student/create Bad response status code")
