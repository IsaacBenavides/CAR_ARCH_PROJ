# Generated by Django 4.0.4 on 2023-06-13 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
    ]
