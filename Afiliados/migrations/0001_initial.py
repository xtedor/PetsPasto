# Generated by Django 3.1.7 on 2021-04-28 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('abreviatura', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('abreviatura', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afiliados.paises')),
            ],
        ),
        migrations.CreateModel(
            name='afiliados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('numero_movil', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afiliados.ciudades')),
            ],
        ),
    ]
