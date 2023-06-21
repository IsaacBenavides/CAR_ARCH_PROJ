from django.db.models import Q
from apps.students.entity import StudentEntity
from apps.students.models import Student


def validate_unique_fields_of_student(student: StudentEntity):
    students = Student.objects.filter(Q(phone=student.phone) | Q(email=student.email))
    return students.count() != 0
