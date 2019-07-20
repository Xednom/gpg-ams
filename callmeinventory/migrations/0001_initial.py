# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_call', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('category', models.CharField(blank=True, choices=[('Buyers', 'Buyers'), ('Sellers', 'Sellers'), ('General Call', 'General Call'), ('Voicemail', 'Voicemail')], max_length=150, null=True)),
                ('client_full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('client_company_name', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile', models.CharField(blank=True, max_length=150, null=True)),
                ('total_handling_time', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_time_transferring_leads', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_mins', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Call Me Inventory',
                'verbose_name_plural': 'Call Me Inventories',
                'ordering': ['-date_of_call'],
            },
        ),
    ]
