# Generated by Django 2.2.26 on 2022-01-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0021_alter_ride_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
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
