# Generated by Django 2.1.7 on 2019-03-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0003_auto_20190306_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='obs',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
