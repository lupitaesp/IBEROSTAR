# Generated by Django 2.2.3 on 2022-08-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinventario', '0015_auto_20220808_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='fecha_compra',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assets',
            name='serie',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]