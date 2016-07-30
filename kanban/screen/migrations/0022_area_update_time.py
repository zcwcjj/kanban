# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0021_auto_20160630_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='update_time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 7, 7, 37, 14, 883696, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
