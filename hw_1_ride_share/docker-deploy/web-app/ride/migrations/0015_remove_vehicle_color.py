# Generated by Django 4.0.1 on 2022-01-23 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0014_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='color',
        ),
    ]
