# Generated by Django 5.0.2 on 2024-03-31 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0015_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='created_at',
        ),
    ]
