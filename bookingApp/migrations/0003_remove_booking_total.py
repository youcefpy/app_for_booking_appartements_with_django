# Generated by Django 5.0.6 on 2024-07-15 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0002_booking_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total',
        ),
    ]