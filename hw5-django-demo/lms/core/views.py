from django.views.generic import FormView
from django.views.generic.list import ListView
from core.models import Group, Teacher, Student
from django.db.models import F
from django.db.models.aggregates import Avg, Count, Max, Min
from core.forms import StudentForm, GroupForm, TeacherForm
from django.shortcuts import get_object_or_404


class IndexView(ListView):
    """
    Show main info about all groups
    """
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
    """
    Show all info about the group
    """
    template_name = "group.html"
    model = Group


class CreateGroupView(FormView):
    """
    Create a new group using the model Group
    """
    template_name = 'create.html'
    form_class = GroupForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateGroupView, self).get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.save()
        return super(CreateGroupView, self).form_valid(form)


class UpdateGroupView(FormView):
    """
    Update the selected group
    """
    template_name = 'create.html'
    form_class = GroupForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        kwargs.update({'instance': group})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateGroupView, self).get_context_data(**kwargs)
        context['button_name'] = 'Update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()
        return super(UpdateGroupView, self).form_valid(form)


class TeacherView(ListView):
    """
    Show all info about teacher using model
    """
    template_name = "teacher.html"
    model = Teacher


class CreateTeacherView(FormView):
    """
    Create a new teacher using the model Teacher
    """
    template_name = 'create.html'
    form_class = TeacherForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateTeacherView, self).get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()
        return super(CreateTeacherView, self).form_valid(form)


class UpdateTeacherView(FormView):
    """
    Update the selected teacher
    """
    template_name = 'create.html'
    form_class = TeacherForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        teacher = get_object_or_404(Teacher, pk=self.kwargs.get('pk'))
        kwargs.update({'instance': teacher})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateTeacherView, self).get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()
        return super(UpdateTeacherView, self).form_valid(form)


class StudentView(ListView):
    template_name = "student.html"
    model = Student


class CreateStudentView(FormView):
    """
    Create a new student using the model Student
    """
    template_name = 'create.html'
    form_class = StudentForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()
        return super(CreateStudentView, self).form_valid(form)


class UpdateStudentView(FormView):
    """
    Update the selected student
    """
    template_name = 'create.html'
    form_class = StudentForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        student = get_object_or_404(Student, pk=self.kwargs.get('pk'))
        kwargs.update({'instance': student})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()
        return super(UpdateStudentView, self).form_valid(form)
