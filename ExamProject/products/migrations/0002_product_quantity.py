# Generated by Django 4.2.3 on 2023-08-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
