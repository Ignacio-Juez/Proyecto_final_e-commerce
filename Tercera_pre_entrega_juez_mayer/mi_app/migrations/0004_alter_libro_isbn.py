# Generated by Django 5.1.1 on 2024-09-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_remove_autor_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(default='0000000000000', max_length=13, unique=True),
        ),
    ]
