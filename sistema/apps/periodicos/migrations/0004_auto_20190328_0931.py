# Generated by Django 2.1.7 on 2019-03-28 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicos', '0003_auto_20190328_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='descripcion',
            field=models.TextField(max_length=255, validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
    ]
