# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog20', '0004_auto_20170921_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='subtitulo',
            field=models.CharField(max_length=200, default='subtitulos'),
            preserve_default=False,
        ),
    ]
