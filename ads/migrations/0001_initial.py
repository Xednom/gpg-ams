# Generated by Django 2.1.2 on 2019-09-24 07:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0012_clients_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date_completed', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('apn_or_items_needs_ad_content', models.TextField(blank=True, null=True)),
                ('client_recommendation', models.TextField(blank=True, help_text="Client's Recommendation of Ad Content Title(If the client wish to give)", null=True)),
                ('content_instruction', models.TextField(blank=True, help_text='Ad/s Content instruction from the Client', null=True)),
                ('content_finished', models.TextField(blank=True, help_text='Ad/s Content finished Ads(From the VA)', null=True)),
                ('final_title', models.TextField(blank=True, help_text='Final title of the Add Content', null=True)),
                ('modification', models.TextField(blank=True, help_text='Any Modification requested by the Client', null=True)),
                ('content_status', models.CharField(choices=[('Client Submitted to the Ad/s Writer', 'Client Submitted to the Ad/s Writer '), ('Ad/s Writer Processing ', 'Ad/s Writer Processing '), ('Ad/s Content Completed ', 'Ad/s Content Completed '), ('Ad/s Content Submitted to the Client', 'Ad/s Content Submitted to the Client'), ('Ad/s Content Closed', 'Ad/s Content Closed')], max_length=150)),
                ('additional_notes', models.TextField(blank=True, help_text='Additional notes from the Ad/s writer', null=True)),
                ('ads_writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Staffs')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Clients')),
            ],
            options={
                'ordering': ['-date_requested'],
            },
        ),
    ]
