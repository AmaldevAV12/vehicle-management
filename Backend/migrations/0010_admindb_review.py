# Generated by Django 4.1.2 on 2023-01-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_remove_admindb_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindb',
            name='Review',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
