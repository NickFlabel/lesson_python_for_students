# Generated by Django 5.1.2 on 2024-10-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_images/'),
        ),
    ]
