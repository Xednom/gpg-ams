# Generated by Django 2.1.2 on 2019-03-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0011_added_tota_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='duediligence',
            name='attachments',
            field=models.URLField(blank=True, null=True),
        ),
    ]
