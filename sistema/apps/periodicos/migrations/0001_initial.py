# Generated by Django 2.1.7 on 2019-03-26 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('ruta', models.ImageField(upload_to='static/images/periodico')),
                ('siglo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Periodico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('anio_inicio', models.IntegerField()),
                ('anio_fin', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodicos.Origen')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='periodico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodicos.Periodico'),
        ),
    ]
