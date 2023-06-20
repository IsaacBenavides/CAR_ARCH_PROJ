from django.shortcuts import render

from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.students.forms import ExcelFileForm
from django.contrib import messages
from apps.students.tasks import read_excel, save_students


# Create your views here.
class HomeView(FormView):
    template_name = "home/home.html"
    form_class = ExcelFileForm

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

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
        return "/"
