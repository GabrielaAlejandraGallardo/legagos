# Generated by Django 5.0.6 on 2024-07-27 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40, verbose_name='Nombre')),
                ('ap', models.CharField(max_length=40, verbose_name='Apellido Paterno')),
                ('am', models.CharField(max_length=40, verbose_name='Apellido Materno')),
                ('dir', models.TextField(null=True, verbose_name='Dirección')),
                ('tel', models.TextField(null=True, verbose_name='Telefono')),
                ('dni', models.ImageField(null=True, upload_to='imagenes/', verbose_name='foto dni')),
                ('isa', models.FileField(null=True, upload_to='user_documents/', verbose_name='isa')),
                ('cus', models.FileField(null=True, upload_to='user_documents/', verbose_name='foto cus')),
            ],
        ),
    ]