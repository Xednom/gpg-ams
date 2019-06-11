# Generated by Django 2.1.2 on 2019-06-11 13:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fillables', '0002_added_va'),
        ('users', '0031_auto_20190611_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=150, null=True)),
                ('company_category', models.CharField(blank=True, choices=[('landmaster.us', 'landmaster.us'), ('gpgcorporations.com', 'gpgcorporations.com'), ('callme.com.ph', 'callme.com.ph'), ('virtualExpressServices.com', 'virtualExpressServices.com'), ('creatif-designs.com', 'creatif-designs.com'), ('vacantpropertiesglobal.com', 'vacantpropertiesglobal.com')], max_length=150, null=True)),
                ('apps_url_link', models.URLField(blank=True, null=True)),
                ('type_of_apps', models.CharField(blank=True, max_length=150, null=True)),
                ('link_to_the_app', models.URLField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=150, null=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('added_by', models.CharField(blank=True, max_length=150, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=150, null=True)),
                ('client_full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Clients')),
                ('give_access_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.VirtualAssistant')),
            ],
            options={
                'verbose_name': 'General Login',
                'verbose_name_plural': 'General Logins',
                'ordering': ['client_full_name'],
            },
        ),
    ]
