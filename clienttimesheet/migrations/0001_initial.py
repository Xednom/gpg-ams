# Generated by Django 2.1.2 on 2019-05-13 08:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fillables', '0002_added_va'),
    ]

    operations = [
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
                ('tax_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('total_tax_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('total_amount_due', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('assigned_job_request_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.VirtualAssistant')),
            ],
            options={
                'verbose_name': 'Client TimeSheet',
                'verbose_name_plural': 'Client TimeSheets',
                'ordering': ['-company_tagging'],
            },
        ),
    ]