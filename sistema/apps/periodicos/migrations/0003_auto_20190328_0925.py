# Generated by Django 2.1.7 on 2019-03-28 14:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicos', '0002_auto_20190328_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='descripcion',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
    ]
