# Generated by Django 4.1.1 on 2022-11-16 19:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0005_profile_direccion_profile_email_profile_municipio_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Peluqueria',
        ),
    ]