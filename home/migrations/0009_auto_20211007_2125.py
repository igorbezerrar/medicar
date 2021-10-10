# Generated by Django 2.2.9 on 2021-10-08 00:25

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211007_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='horario',
        ),
        migrations.AddField(
            model_name='agenda',
            name='horas',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='_agenda_horas_+', to='home.Agenda'),
        ),
    ]
