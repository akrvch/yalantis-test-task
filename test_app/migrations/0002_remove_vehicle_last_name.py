# Generated by Django 3.0 on 2021-12-09 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='last_name',
        ),
    ]
