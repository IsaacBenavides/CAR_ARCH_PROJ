from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import generics
from apps.students.api.serializers import StudentSerializer
from apps.students.models import Student


class StudentsAPIView(generics.ListAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
