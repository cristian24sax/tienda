# Generated by Django 3.1.5 on 2021-06-19 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('user_modifc', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=100, unique=True)),
                ('direction', models.CharField(blank=True, max_length=250, null=True)),
                ('contact', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
