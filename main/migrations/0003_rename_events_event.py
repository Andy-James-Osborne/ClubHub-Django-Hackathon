# Generated by Django 4.2.11 on 2024-03-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_post_comment_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
