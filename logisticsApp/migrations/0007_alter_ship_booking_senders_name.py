# Generated by Django 4.1.6 on 2023-02-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsApp', '0006_alter_ship_booking_senders_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship_booking',
            name='senders_name',
            field=models.CharField(max_length=250),
        ),
    ]
