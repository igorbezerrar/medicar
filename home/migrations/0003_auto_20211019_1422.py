# Generated by Django 2.2.9 on 2021-10-19 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211019_1353'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='agenda',
            name='dia__gte',
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.CheckConstraint(check=models.Q(dia__gte=datetime.datetime(2021, 10, 19, 17, 21, 40, 531572, tzinfo=utc)), name='dia__gte'),
        ),
    ]
