# Generated by Django 3.2.4 on 2021-07-19 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210719_0736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]