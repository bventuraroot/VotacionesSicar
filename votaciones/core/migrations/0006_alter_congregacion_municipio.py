# Generated by Django 4.1.2 on 2022-10-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_congregacion_municio_congregacion_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacion',
            name='municipio',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
