# Generated by Django 4.0.1 on 2022-01-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0015_remove_vehicle_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(default='abc', max_length=7, unique=True),
            preserve_default=False,
        ),
    ]