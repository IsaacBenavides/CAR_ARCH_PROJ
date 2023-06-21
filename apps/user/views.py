from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView, View
from apps.user.forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from drf_yasg.utils import swagger_auto_schema


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True

    @swagger_auto_schema(request_body=LoginForm)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(self.get_success_url())
                else:
                    messages.error(request, "Credenciales incorrectas")
            else:
                return render(request, self.template_name, {"form": form})
        return render(request, self.template_name, {"form": form})

    @swagger_auto_schema()
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def get_success_url(self) -> str:
        return "/students/load/"


class SignUpView(FormView):
    template_name = "user/register.html"
    form_class = SignUpForm

    @swagger_auto_schema(request_body=SignUpForm)
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect(self.get_success_url())
            else:
                return render(request, self.template_name, {"form": form})
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    @swagger_auto_schema()
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def get_success_url(self) -> str:
        return "/login/"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")


class CloseMessages(View):
    def get(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        return redirect("/login/")
