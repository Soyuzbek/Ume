# Generated by Django 2.2.1 on 2019-05-26 10:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190524_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
    ]
