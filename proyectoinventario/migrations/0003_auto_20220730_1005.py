# Generated by Django 2.2.3 on 2022-07-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinventario', '0002_auto_20220723_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]