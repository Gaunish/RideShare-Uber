# Generated by Django 2.2.26 on 2022-01-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0005_alter_user_id_alter_vehicle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
