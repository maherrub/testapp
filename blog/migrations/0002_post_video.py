# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-07 08:15
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/blog', validators=[blog.validators.validate_videoitem_extension]),
        ),
    ]
