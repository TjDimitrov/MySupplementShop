# Generated by Django 4.2.3 on 2023-08-03 10:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_storeuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeuser',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
