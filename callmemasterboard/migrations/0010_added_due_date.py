# Generated by Django 2.1.2 on 2019-07-31 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callmemasterboard', '0009_added_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterboard',
            name='due_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]