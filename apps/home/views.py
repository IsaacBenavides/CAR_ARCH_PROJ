from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.home.forms import ExcelFileForm
from django.contrib import messages


class HomeView(FormView):
    template_name = "home/home.html"
    form_class = ExcelFileForm

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        messages.success(request, "Nice :3")

        return super().post(request, *args, **kwargs)
