# Generated by Django 5.0.2 on 2024-10-26 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_todo_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 26, 7, 59, 52, 477837)),
        ),
    ]