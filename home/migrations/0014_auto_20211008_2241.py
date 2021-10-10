# Generated by Django 2.2.9 on 2021-10-09 01:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211007_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horas',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=49),
        ),
    ]
