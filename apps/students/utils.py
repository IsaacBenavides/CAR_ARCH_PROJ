from django.db.models import Q
from apps.students.entity import StudentEntity
from apps.students.models import Student


def add_errors(key, value):
    errors = {}
    if key in errors.values():
        errors[key].append(value)
    else:
        errors[key] = [value]
    return errors


def validate_unique_fields_of_student(student: StudentEntity):
    students = Student.objects.filter(Q(phone=student.phone) | Q(email=student.email))
    return students.count() != 0
