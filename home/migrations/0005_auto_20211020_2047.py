# Generated by Django 2.2.9 on 2021-10-20 23:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211019_2105'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='agenda',
            name='dia__gte',
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.CheckConstraint(check=models.Q(dia__gte=datetime.datetime(2021, 10, 20, 23, 47, 51, 246629, tzinfo=utc)), name='dia__gte'),
        ),
        migrations.AddConstraint(
            model_name='consultas',
            constraint=models.CheckConstraint(check=models.Q(dia__gte=datetime.datetime(2021, 10, 20, 23, 47, 51, 246629, tzinfo=utc)), name='dia__gte'),
        ),
    ]
