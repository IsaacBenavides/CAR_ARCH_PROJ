from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.students.forms import ExcelFileForm
from django.contrib import messages
from apps.students.tasks import read_excel, save_students
from drf_yasg.utils import swagger_auto_schema


class LoadStudents(FormView):
    template_name = "home/home.html"
    form_class = ExcelFileForm

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, *args, **kwargs):
        return super(LoadStudents, self).dispatch(*args, **kwargs)

    @swagger_auto_schema(request_body=ExcelFileForm)
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.method == "POST":
            form = ExcelFileForm(request.POST, request.FILES)
            if form.is_valid():
                students = read_excel(request.FILES["excel"].read())
                save_students.delay(students, request.user.email)
                messages.success(
                    request,
                    "Archivo recibido. Le avisaremos por email cuando hayamos terminado de procesarlo.",
                )
            else:
                messages.error(request, "Hubo un error.")

        return super().post(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return "/students/load/"
