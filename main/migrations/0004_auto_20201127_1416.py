# Generated by Django 2.2 on 2020-11-27 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201127_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 14, 16, 8, 231863, tzinfo=utc)),
        ),
    ]
