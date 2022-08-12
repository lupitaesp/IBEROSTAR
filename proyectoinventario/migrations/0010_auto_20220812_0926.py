# Generated by Django 2.2.3 on 2022-08-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinventario', '0009_auto_20220812_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='cliente',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='equipo',
            field=models.CharField(default=0, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]