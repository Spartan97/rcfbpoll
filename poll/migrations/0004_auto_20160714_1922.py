# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-15 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20160714_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='flair',
            field=models.FilePathField(match='\\.png', path='E:\\workspace\\rcfbpoll\\rcfbpoll\\staticfiles\\images/full60', recursive=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='header',
            field=models.FilePathField(match='\\.png', path='E:\\workspace\\rcfbpoll\\rcfbpoll\\staticfiles\\images/header240', recursive=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.FilePathField(match='\\.png', path='E:\\workspace\\rcfbpoll\\rcfbpoll\\staticfiles\\images/fullorig', recursive=True),
        ),
    ]