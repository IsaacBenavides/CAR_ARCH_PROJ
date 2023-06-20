from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.courses.models import Course


class Student(models.Model):
    class GenderChoices(models.TextChoices):
        male = ("masculino", "Masculino")
        female = ("femenino", "Femenino")
        other = ("otro", "Otro")

    class AdmitionStatusChoices(models.TextChoices):
        admitted = "admitido", "Admitido"
        refused = "rechazado", "Rechazado"
        pending = "pendiente", "Pendiente"
        graduated = "egresado", "Egresado"

    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False)
    gender = models.TextField(
        choices=GenderChoices.choices,
        default=GenderChoices.male,
        blank=False,
        null=False,
    )
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    date_of_admition = models.DateField(blank=False, null=False)
    admition_status = models.CharField(
        choices=AdmitionStatusChoices.choices,
        default=AdmitionStatusChoices.pending,
        max_length=50,
    )
    email = models.EmailField(unique=True, blank=True, null=True)
    course = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"
