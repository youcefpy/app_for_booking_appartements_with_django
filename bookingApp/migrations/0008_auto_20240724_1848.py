# Generated by Django 3.2.25 on 2024-07-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0007_appartimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appartimages',
            name='appartement',
        ),
        migrations.AddField(
            model_name='appartment',
            name='list_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingApp.appartimages'),
        ),
    ]
