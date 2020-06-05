# Generated by Django 2.1.7 on 2019-03-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0004_auto_20190306_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images/')),
                ('foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fotos.Foto')),
            ],
        ),
    ]