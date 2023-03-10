# Generated by Django 4.1.6 on 2023-03-10 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsApp', '0016_alter_delivery_destination_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery_destination',
            options={'ordering': ['-location']},
        ),
        migrations.AddField(
            model_name='delivery_destination',
            name='tracking_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsApp.ship_booking'),
        ),
    ]