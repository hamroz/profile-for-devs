# Generated by Django 3.2.9 on 2021-11-11 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_tags1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='tags1',
            new_name='tags',
        ),
    ]
