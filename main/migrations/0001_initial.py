# Generated by Django 2.1.7 on 2019-04-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('state', models.CharField(choices=[('ZD', 'Necessary'), ('SD', 'Optional')], max_length=5, verbose_name='type')),
                ('term', models.PositiveSmallIntegerField(default=1, verbose_name='term')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
                ('content', models.TextField(verbose_name='content')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('expire', models.DateTimeField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('annotation', models.TextField(verbose_name='annotation')),
                ('content', models.TextField(verbose_name='content')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]