# Generated by Django 2.1.7 on 2019-03-28 14:54

import apps.expedientes.validadores
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('legajo', models.CharField(max_length=5)),
                ('numero', models.CharField(max_length=9)),
                ('descripcion', models.TextField(blank=True, max_length=300, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('folios', models.IntegerField()),
                ('fecha_ext1', models.DateField()),
                ('fecha_ext2', models.DateField()),
                ('ruta', models.ImageField(blank=True, null=True, upload_to='static/images/expedientes')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=32, validators=[apps.expedientes.validadores.minimo])),
                ('nombre', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipoexpediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='expediente',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expedientes.Serie'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='tipoexpediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expedientes.Tipoexpediente'),
        ),
    ]
