# Generated by Django 4.1.6 on 2023-03-10 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logisticsApp', '0014_rename_status_delivery_destination_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_destination',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]