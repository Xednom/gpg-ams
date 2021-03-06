# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerReminders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('manager_under', models.CharField(blank=True, max_length=150, null=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(blank=True, max_length=150, null=True)),
                ('notes_from_company', models.TextField()),
                ('notes_from_manager', models.TextField()),
            ],
            options={
                'verbose_name': 'Manager Reminder',
                'verbose_name_plural': 'Manager Reminders',
                'ordering': ['-date'],
            },
        ),
    ]
