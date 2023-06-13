from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    speciality = models.CharField(max_length=50, blank=True, null=True)
