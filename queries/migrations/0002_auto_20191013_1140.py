# Generated by Django 2.1.5 on 2019-10-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask_question',
            name='code',
            field=models.TextField(null=True),
        ),
    ]
