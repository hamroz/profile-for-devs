# Generated by Django 3.2.9 on 2021-11-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_owner'),
        ('users', '0004_rename_tags1_profile_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.Project'),
        ),
    ]