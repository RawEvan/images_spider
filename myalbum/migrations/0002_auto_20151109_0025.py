# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myalbum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgstorage',
            old_name='originalUrl',
            new_name='original_url',
        ),
        migrations.RenameField(
            model_name='imgstorage',
            old_name='storageUrl',
            new_name='storage_url',
        ),
    ]
