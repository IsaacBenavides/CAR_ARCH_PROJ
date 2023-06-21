from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from apps.students.models import Student
from apps.courses.models import Course


class LoadCourses(TemplateView):
    template_name = "courses/load_courses.html"

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, *args, **kwargs):
        return super(LoadCourses, self).dispatch(*args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.method == "POST":
            try:
                messages.success(
                    request,
                    "Empezamos a obtener los cursos. Te enviaremos un email cuando hayamos terminado.",
                )
            except:
                messages.error(
                    request,
                    "Hubo un error",
                )
        return redirect(self.get_success_url())

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        students = Student.objects.all()
        courses = Course.objects.all()
        if courses.count() != 0:
            return redirect("/students/load/")
        elif students.count() != 0:
            return redirect("/students/load/")
        return render(
            request,
            self.template_name,
        )

    def get_success_url(self) -> str:
        return "/courses/load/"
