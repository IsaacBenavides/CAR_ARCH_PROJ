from django.db import models
from apps.students.models import Student
from apps.courses.models import Course
from apps.teacher.models import Teacher


class Rating(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=False, null=False
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=False, null=False
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=False, null=False
    )
    rating = models.DecimalField(
        blank=False, null=False, decimal_places=2, max_digits=3
    )
