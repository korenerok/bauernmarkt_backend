# Generated by Django 3.0.2 on 2020-03-06 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200129_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalog',
            new_name='Item',
        ),
    ]
