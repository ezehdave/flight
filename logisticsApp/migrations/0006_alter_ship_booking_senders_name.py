# Generated by Django 4.1.6 on 2023-02-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsApp', '0005_ship_booking_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship_booking',
            name='senders_name',
            field=models.TextField(max_length=250),
        ),
    ]
