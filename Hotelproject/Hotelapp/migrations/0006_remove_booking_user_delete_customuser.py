# Generated by Django 5.0.2 on 2024-12-09 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelapp', '0005_customuser_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]