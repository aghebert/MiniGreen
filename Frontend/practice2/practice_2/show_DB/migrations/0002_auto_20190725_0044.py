# Generated by Django 2.2.3 on 2019-07-25 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemhistory',
            name='date_bought',
            field=models.DateField(default=datetime.date(2019, 7, 25)),
        ),
        migrations.AlterField(
            model_name='itemhistory',
            name='date_sold',
            field=models.DateField(default=datetime.date(2019, 7, 25)),
        ),
    ]
