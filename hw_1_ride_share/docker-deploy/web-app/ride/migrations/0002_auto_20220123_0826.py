# Generated by Django 2.2.26 on 2022-01-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
