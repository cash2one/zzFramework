# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KWD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='browser',
            name='browser',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='browser',
            name='profile',
            field=models.FileField(upload_to=b'./upload/', blank=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='browser',
            field=models.ForeignKey(blank=True, to='KWD.Browser', null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='by',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='sleep',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='url',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='value',
            field=models.TextField(null=True, blank=True),
        ),
    ]
