# Generated by Django 4.2.3 on 2023-08-15 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoupSwap_App', '0006_coupon_requestedby_coupon_usedby'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CouponRequests',
        ),
    ]
