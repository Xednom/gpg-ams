# Generated by Django 2.1.2 on 2019-04-17 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vapayroll',
            name='time_in',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='vapayroll',
            name='time_out',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]