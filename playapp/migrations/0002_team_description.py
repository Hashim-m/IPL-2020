# Generated by Django 3.0 on 2020-09-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
