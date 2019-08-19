# Generated by Django 2.1.2 on 2019-08-19 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callmemasterboard', '0012_masterboard_monthly_plan_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterboard',
            name='client_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Clients'),
        ),
    ]
