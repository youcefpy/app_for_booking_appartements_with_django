# Generated by Django 5.0.6 on 2024-07-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]