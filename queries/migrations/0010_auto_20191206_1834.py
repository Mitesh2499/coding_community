# Generated by Django 2.1.5 on 2019-12-06 13:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queries', '0009_auto_20191206_0730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diussion_Like',
            new_name='Dicussion_Like',
        ),
    ]