from django import forms
from django.core.validators import FileExtensionValidator


class ExcelFileForm(forms.Form):
    excel = forms.FileField(
        required=True,
        label="Selecciona un archivo",
        validators=[
            FileExtensionValidator(
                ["xlsx", "csv", "xls"],
            ),
        ],
        widget=forms.FileInput(
            attrs={
                "accept": ".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel",
                "class": "input-excel",
            }
        ),
    )
