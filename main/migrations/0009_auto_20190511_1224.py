# Generated by Django 2.1.7 on 2019-05-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190511_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='annotation',
            field=models.TextField(verbose_name='annotation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='annotation_en',
            field=models.TextField(null=True, verbose_name='annotation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='annotation_ru',
            field=models.TextField(null=True, verbose_name='annotation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
    ]
