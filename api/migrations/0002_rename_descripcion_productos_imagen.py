# Generated by Django 4.2.7 on 2023-12-06 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='Descripcion',
            new_name='Imagen',
        ),
    ]
