# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KWD', '0002_auto_20160525_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='case',
            field=models.ForeignKey(default=None, to='KWD.Case'),
            preserve_default=False,
        ),
    ]
