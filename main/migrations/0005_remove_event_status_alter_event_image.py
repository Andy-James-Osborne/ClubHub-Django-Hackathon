# Generated by Django 4.2.11 on 2024-03-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_event_body_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='event_images'),
        ),
    ]