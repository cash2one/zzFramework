# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('browser', models.CharField(max_length=20)),
                ('profile', models.FileField(upload_to=b'./upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('createtime', models.DateTimeField()),
                ('modifytime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=500)),
                ('by', models.CharField(max_length=20)),
                ('value', models.TextField()),
                ('sleep', models.IntegerField()),
                ('action', models.ForeignKey(to='KWD.Action')),
                ('browser', models.ForeignKey(to='KWD.Browser')),
            ],
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('createtime', models.DateTimeField()),
                ('modifytime', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='suite',
            field=models.ForeignKey(to='KWD.Suite'),
        ),
    ]
