# Generated by Django 4.0.1 on 2022-01-30 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0035_auto_20220130_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='capacity_remaining',
            new_name='capacity',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='sharer',
        ),
        migrations.AlterField(
            model_name='ride',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=1)),
                ('is_sharer', models.BooleanField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ride', to='ride.ride')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rider', to='ride.user')),
            ],
        ),
    ]
