# Generated by Django 2.1.2 on 2019-07-09 05:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('craigslist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CraiglistPosting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_posted', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('apn', models.CharField(blank=True, max_length=150, null=True)),
                ('cl_memo_post', models.TextField(blank=True, null=True)),
                ('cl_url_link', models.CharField(blank=True, max_length=150, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cl_admin_support', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Staffs')),
            ],
            options={
                'verbose_name': 'Craiglist Posting',
                'verbose_name_plural': 'Craiglist Postings',
                'ordering': ['-date_posted'],
            },
        ),
    ]