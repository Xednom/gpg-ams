# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_sign_up', models.DateField(blank=True, null=True)),
                ('client_company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('agreed_hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('client_code', models.CharField(blank=True, max_length=150, null=True)),
                ('client_phone_number', models.CharField(blank=True, max_length=150, null=True)),
                ('client_email', models.EmailField(blank=True, max_length=250, null=True)),
                ('referred_by', models.CharField(blank=True, max_length=250, null=True)),
                ('clients_count_number', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'List of Client Job',
                'verbose_name_plural': 'List of Client Jobs',
                'ordering': ['-date_sign_up'],
            },
        ),
    ]
