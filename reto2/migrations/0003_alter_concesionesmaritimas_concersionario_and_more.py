# Generated by Django 4.0 on 2023-06-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reto2', '0002_concesionesmaritimas_fecha_creacion_dato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concesionesmaritimas',
            name='concersionario',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='concesionesmaritimas',
            name='lugar',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='concesionesmaritimas',
            name='tipo_vigencia',
            field=models.CharField(max_length=200),
        ),
    ]
