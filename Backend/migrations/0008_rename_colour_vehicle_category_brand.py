# Generated by Django 4.1.2 on 2023-01-04 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_admindb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle_category',
            old_name='Colour',
            new_name='Brand',
        ),
    ]
