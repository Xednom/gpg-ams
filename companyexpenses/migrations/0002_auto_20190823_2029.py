# Generated by Django 2.1.2 on 2019-08-23 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyexpenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['-date'], 'verbose_name': 'General Expense Inventory', 'verbose_name_plural': 'General Expense Inventories'},
        ),
    ]