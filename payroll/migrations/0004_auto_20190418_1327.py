# Generated by Django 2.1.2 on 2019-04-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_remove_vapayroll_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='vapayroll',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='vapayroll',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Salary = Total hours * Hourly rate', max_digits=7, null=True),
        ),
    ]