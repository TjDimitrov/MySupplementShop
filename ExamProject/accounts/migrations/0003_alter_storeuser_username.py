# Generated by Django 4.2.3 on 2023-08-01 08:07

import ExamProject.accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_storeuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeuser',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[ExamProject.accounts.models.only_nums_and_letters, django.core.validators.MinLengthValidator(5)]),
        ),
    ]
