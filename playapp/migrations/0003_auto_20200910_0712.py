# Generated by Django 3.0 on 2020-09-10 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0002_team_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='Squad',
        ),
    ]
