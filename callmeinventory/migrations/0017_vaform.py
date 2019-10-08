# Generated by Django 2.1.2 on 2019-09-19 11:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_clients_notes'),
        ('callmeinventory', '0016_auto_20190725_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('type_of_script', models.CharField(blank=True, choices=[('Buyer', 'Buyer'), ('Seller', 'Seller'), ('Propert Management', 'Propert Management'), ('General Calls', 'General Calls')], max_length=150, null=True)),
                ('script_link', models.CharField(blank=True, max_length=500, null=True)),
                ('gs_integration', models.CharField(blank=True, max_length=250, null=True)),
                ('client_call_forwarding_number', models.CharField(blank=True, max_length=150, null=True)),
                ('company_call_forwarding_number', models.CharField(blank=True, max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client_full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Clients')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]