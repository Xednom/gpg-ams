# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Company name',
                'verbose_name_plural': 'Company names',
            },
        ),
        migrations.CreateModel(
            name='DateInformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weeks', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InternalCompanyName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Internal Company Names',
            },
        ),
        migrations.CreateModel(
            name='JobTitleRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'List of Job title request',
                'verbose_name_plural': 'List of Job title requests',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lead_source', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Lead Source',
                'verbose_name_plural': 'Lead Sources',
            },
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_manager', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SeniorManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=250)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'List of Task',
                'verbose_name_plural': 'List of Tasks',
            },
        ),
        migrations.CreateModel(
            name='TypeOfTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'List of Type of Task',
                'verbose_name_plural': 'List of Type of Tasks',
            },
        ),
        migrations.CreateModel(
            name='VirtualAssistant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'List of VA',
                'verbose_name_plural': 'List of VAs',
            },
        ),
    ]
