# Generated by Django 2.1.2 on 2019-08-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmefinancialreport', '0005_added_moneyfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialreport',
            name='monthly_plan_cost',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]