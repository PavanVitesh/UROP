# Generated by Django 4.2.3 on 2023-11-27 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoupSwap_App', '0008_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='TranDate',
            field=models.DateField(default=datetime.date(2023, 11, 27), verbose_name='Transaction Date'),
        ),
    ]
