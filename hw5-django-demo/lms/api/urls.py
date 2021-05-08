from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupList.as_view()),
    path('students/',
         views.StudentViewSet.as_view(
             {'get': 'list',
              'post': 'create'}
         )),
    path('students/<int:pk>/',
         views.StudentViewSet.as_view(
             {'get': 'retrieve',
              'put': 'update',
              'delete': 'destroy'}
         )),
    path('teachers/', views.TeacherViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('teachers/<int:pk>/', views.TeacherViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'delete': 'destroy'}
    )),
]

urlpatterns = format_suffix_patterns(urlpatterns)
