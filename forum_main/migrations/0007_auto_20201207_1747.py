# Generated by Django 3.1.4 on 2020-12-07 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0006_auto_20201207_1745'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]