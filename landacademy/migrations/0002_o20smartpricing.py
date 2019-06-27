# Generated by Django 2.1.2 on 2019-06-27 14:09

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('landacademy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='O20SmartPricing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('situs_address', models.TextField(blank=True, null=True)),
                ('trulia', models.CharField(blank=True, max_length=150, null=True)),
                ('zillow', models.CharField(blank=True, max_length=150, null=True)),
                ('redfin', models.CharField(blank=True, max_length=150, null=True)),
                ('realfor', models.CharField(blank=True, max_length=150, null=True)),
                ('realtytrac', models.CharField(blank=True, max_length=150, null=True)),
                ('encoder', models.CharField(blank=True, max_length=150, null=True)),
                ('date_encoded', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('quality_check_status', models.CharField(blank=True, choices=[('Complete', 'Complete'), ('Complete Incorrect Data Input', 'Complete Incorrect Data Input'), ('Others', 'Others')], max_length=25, null=True)),
                ('quality_specialist', models.CharField(blank=True, max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Land Academy O20 Smart Pricing',
                'verbose_name_plural': 'Land Academy O20 Smart Pricings',
                'ordering': ['-date_encoded'],
            },
        ),
    ]
