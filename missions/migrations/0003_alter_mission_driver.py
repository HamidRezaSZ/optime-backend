# Generated by Django 4.2.2 on 2023-06-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_driver_free'),
        ('missions', '0002_mission_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver', verbose_name='راننده'),
        ),
    ]
