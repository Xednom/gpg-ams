# Generated by Django 2.1.2 on 2019-06-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmeinventory', '0009_auto_20190630_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='call_duration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='total_time_transferring_leads',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]