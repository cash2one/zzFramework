# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KWD', '0004_auto_20160527_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('model', models.CharField(max_length=200, choices=[(b'1', b'Project'), (b'2', b'Suite'), (b'3', b'Case'), (b'4', b'Step')])),
                ('operate', models.CharField(max_length=200, choices=[(b'1', b'Create'), (b'2', b'Modify'), (b'3', b'Delete')])),
                ('be_operated', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='case',
            old_name='name',
            new_name='case',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='suite',
            old_name='name',
            new_name='suite',
        ),
        migrations.AddField(
            model_name='case',
            name='creator',
            field=models.ForeignKey(default=None, to='KWD.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='file',
            field=models.FileField(upload_to=b'./upload/', blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='memo',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.CharField(blank=True, max_length=10, choices=[(b'API', '\u63a5\u53e3\u6d4b\u8bd5\u7528\u4f8b'), (b'UI', 'UI\u6d4b\u8bd5\u7528\u4f8b')]),
        ),
        migrations.AddField(
            model_name='step',
            name='creator',
            field=models.ForeignKey(default=1, to='KWD.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='memo',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='suite',
            name='creator',
            field=models.ForeignKey(default=1, to='KWD.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suite',
            name='memo',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='suite',
            name='project',
            field=models.ForeignKey(default=1, to='KWD.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='modifytime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='suite',
            field=models.ForeignKey(to='KWD.Suite', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='memo',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='browser',
            field=models.ForeignKey(default=1, blank=True, to='KWD.Browser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='step',
            name='by',
            field=models.CharField(default=1, max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='step',
            name='url',
            field=models.CharField(default=1, max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='step',
            name='value',
            field=models.TextField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suite',
            name='modifytime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(to='KWD.User'),
        ),
    ]
