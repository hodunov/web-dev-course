"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core.views import GroupView, TeacherView, StudentView, IndexView
from core.views import CreateGroupView, CreateTeacherView, CreateStudentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/',include(debug_toolbar.urls)),
    path('',IndexView.as_view(template_name='group_detail.html')),
    path('group/', GroupView.as_view()),
    path('teacher/', TeacherView.as_view()),
    path('student/', StudentView.as_view()),
    path('group/create/', CreateGroupView.as_view()),
    path('teacher/create/', CreateTeacherView.as_view()),
    path('student/create/', CreateStudentView.as_view()),
]
