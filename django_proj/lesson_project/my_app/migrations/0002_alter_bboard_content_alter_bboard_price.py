# Generated by Django 5.1.1 on 2024-10-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bboard',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bboard',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
