# Generated by Django 2.2.7 on 2019-11-09 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(blank=True, verbose_name=datetime.datetime(2019, 11, 9, 14, 54, 6, 391217))),
            ],
        ),
    ]
