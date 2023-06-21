import io
import json
import logging
import pandas as pd
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from apps.students.models import Student
from apps.students.entity import StudentEntity
from apps.students.constants import Constants
from apps.students.utils import validate_unique_fields_of_student

errors = {}


def read_excel(file):
    df = pd.read_excel(io.BytesIO(file))
    students = df.to_json(orient="records", lines=True, force_ascii=False)
    students = students.split("\n")
    return students


@shared_task()
def save_students(students, email=""):
    for student in students:
        try:
            decoded_student = json.loads(student)
            student_entity = StudentEntity(decoded_student)
            if student_entity.has_errors():
                if Constants.empty_fields in errors.keys():
                    errors[Constants.empty_fields].append(student_entity.to_string())
                else:
                    errors[Constants.empty_fields] = [student_entity.to_string()]
            elif validate_unique_fields_of_student(student_entity):
                if Constants.repeat_fields in errors.keys():
                    errors[Constants.repeat_fields].append(student_entity.to_string())
                else:
                    errors[Constants.repeat_fields] = [student_entity.to_string()]
            else:
                Student.objects.get_or_create(
                    name=student_entity.name,
                    last_name=student_entity.last_name,
                    date_of_birth=student_entity.date_of_birth,
                    age=student_entity.age,
                    gender=student_entity.gender,
                    phone=student_entity.phone,
                    date_of_admition=student_entity.date_of_admition,
                    admition_status=student_entity.admition_status,
                    email=student_entity.email,
                )
        except Exception as e:
            logging.error(e)

    send_email_to_user(email, errors)


def send_email_to_user(email, errors={}):
    template_email = "email/success_students_loaded.html"
    email_subject = "Cargado de Estudiantes Existoso"
    if len(errors.keys()) != 0:
        template_email = "email/error_students_failed.html"
        email_subject = "Cargado de Estudiantes Fallido"

    msg_html = render_to_string(
        template_email,
        errors,
    )
    try:
        send_mail(
            email_subject,
            "",
            settings.EMAIL_HOST_USER,
            [email],
            html_message=msg_html,
        )
    except Exception as e:
        logging.error(e)
