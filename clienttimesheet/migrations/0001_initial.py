# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fillables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, help_text='Date the payment made.', null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('reference', models.CharField(blank=True, max_length=150, null=True)),
                ('payment_channel', models.CharField(blank=True, max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Payment Made for the Client',
                'verbose_name_plural': 'Payment Made for the Clients',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_tagging', models.CharField(blank=True, max_length=150, null=True)),
                ('shift_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('month_to_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('clients_full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('title_job_request', models.CharField(blank=True, max_length=150, null=True)),
                ('job_request', models.CharField(blank=True, max_length=150, null=True)),
                ('time_in', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('time_out', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('duration', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('total_items', models.CharField(blank=True, max_length=150, null=True)),
                ('additional_comments', models.TextField(blank=True, null=True)),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('amount_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('tax_fee', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('total_tax_fee', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('total_amount_due', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved')], default='Not Approved', max_length=50)),
                ('assigned_job_request_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.VirtualAssistant')),
            ],
            options={
                'verbose_name': 'Client TimeSheet',
                'verbose_name_plural': 'Client TimeSheets',
                'ordering': ['-company_tagging'],
            },
        ),
    ]
