# Generated by Django 2.2 on 2019-04-26 05:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190426_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='Departure',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 5, 3, 29, 408579, tzinfo=utc)),
        ),
    ]
