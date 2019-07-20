# Generated by Django 2.1.2 on 2019-06-27 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CraiglistInventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_company_name', models.CharField(blank=True, max_length=150, null=True)),
                ('cl_admin_support', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('posted_ads', models.CharField(blank=True, max_length=150, null=True)),
                ('flagged_ads', models.CharField(blank=True, max_length=150, null=True)),
                ('sticked_ads', models.CharField(blank=True, max_length=150, null=True)),
                ('stick_rates', models.CharField(blank=True, max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Craigslist Inventory Record',
                'verbose_name_plural': 'Craigslist Inventory Records',
                'ordering': ['-date'],
            },
        ),
    ]
