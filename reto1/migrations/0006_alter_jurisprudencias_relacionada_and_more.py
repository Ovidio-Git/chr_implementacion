# Generated by Django 4.0 on 2023-06-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reto1', '0005_alter_jurisprudencias_nombre_proyecto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='relacionada',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='item',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='parametro',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='valor',
            field=models.CharField(max_length=700, null=True),
        ),
    ]