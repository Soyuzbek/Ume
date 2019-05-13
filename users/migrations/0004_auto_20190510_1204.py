# Generated by Django 2.1.7 on 2019-05-10 12:04

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190510_1159'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher_en',
            field=models.BooleanField(default=False, verbose_name='is teacher'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher_ru',
            field=models.BooleanField(default=False, verbose_name='is teacher'),
        ),
    ]
