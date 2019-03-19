# Generated by Django 2.1.2 on 2019-03-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0006_changed_recorder_clerk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duediligence',
            name='date_completed_or_returned',
        ),
        migrations.AddField(
            model_name='duediligence',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='notes_from_land_master_team',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='notes_from_the_client',
            field=models.TextField(blank=True, null=True),
        ),
    ]
