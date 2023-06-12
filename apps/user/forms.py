from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        validators=[validators.MinLengthValidator(5)],
        widget=forms.TextInput(
            attrs={
                "id": "username",
                "name": "username",
                "type": "text",
                "class": "form-field",
                "placeholder": "Usuario",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        validators=[validators.MinLengthValidator(5)],
        widget=forms.TextInput(
            attrs={
                "id": "password",
                "name": "password",
                "type": "password",
                "class": "form-field",
                "placeholder": "Contraseña",
            }
        ),
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        validators=[validators.MinLengthValidator(5)],
        widget=forms.TextInput(
            attrs={
                "id": "username",
                "name": "username",
                "type": "text",
                "class": "form-field",
                "placeholder": "Usuario",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator()],
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "name": "email",
                "type": "text",
                "class": "form-field",
                "placeholder": "Correo Electrónico",
            }
        ),
    )

    password1 = forms.CharField(
        required=True,
        validators=[validators.MinLengthValidator(5)],
        widget=forms.TextInput(
            attrs={
                "id": "password",
                "name": "password",
                "type": "password",
                "class": "form-field",
                "placeholder": "Contraseña",
            }
        ),
    )

    password2 = forms.CharField(
        required=True,
        validators=[validators.MinLengthValidator(5)],
        widget=forms.TextInput(
            attrs={
                "id": "confirm_password",
                "name": "confirm_password",
                "type": "password",
                "class": "form-field",
                "placeholder": "Confirmar Contraseña",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
