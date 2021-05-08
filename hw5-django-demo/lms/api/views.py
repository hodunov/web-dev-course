from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    SAFE_METHODS,
)

from core.models import (
    Group,
    Student,
    Teacher,
)
from api.serializers import (
    GroupSerializer,
    StudentSerializer,
    TeacherSerializer,
)


class GroupList(APIView):
    """
    List all groups, or create a new group.
    """
    def get(self, request, format=None):
        snippets = Group.objects.all()
        serializer = GroupSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


class TeacherViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

