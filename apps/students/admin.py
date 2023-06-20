from django.contrib import admin
from apps.students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ["delete_all_registers"]

    def delete_all_registers(self, request, _):
        Student.objects.all().delete()
