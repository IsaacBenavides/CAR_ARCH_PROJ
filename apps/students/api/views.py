from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import generics
from apps.students.api.serializers import StudentSerializer
from apps.students.models import Student
from drf_yasg.utils import swagger_auto_schema


class StudentsAPIView(generics.ListAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    @swagger_auto_schema()
    def get_queryset(self):
        return super().get_queryset()
