# Generated by Django 5.1.1 on 2024-10-09 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('bodega', models.CharField(max_length=100)),
                ('varietal', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maridaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='maridajes/')),
                ('comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maridaje.comida')),
                ('vino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maridaje.vino')),
            ],
        ),
    ]
