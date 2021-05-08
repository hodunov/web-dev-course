import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from core.views import (
    GroupView, TeacherView, StudentView,  IndexView,
    ContactUsView, export_students_csv
)
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', IndexView.as_view(template_name='group_detail.html')),
    path('group/', GroupView.as_view()),
    path('teacher/', TeacherView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/csv', export_students_csv, name="export_students_csv"),
    path('student/', StudentView.as_view()),
    path('contact_us/', ContactUsView.as_view(), name="contact_us"),
    path('contact_us/done/', TemplateView.as_view(
        template_name="contact_done.html"),
         name="contact_done"
         ),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('api.urls')),
]
