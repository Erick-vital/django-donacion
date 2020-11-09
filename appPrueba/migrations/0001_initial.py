# Generated by Django 3.0.8 on 2020-10-23 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloTareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CheckboxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkbox', models.BooleanField(default=False)),
                ('relacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appPrueba.ModeloTareas')),
            ],
        ),
    ]