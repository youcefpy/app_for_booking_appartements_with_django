# Generated by Django 3.2.25 on 2024-08-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0004_commentroom_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentroom',
            options={'ordering': ['-created_on']},
        ),
    ]
