# Generated by Django 2.1.2 on 2019-05-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_added_faqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='lynkcapital',
            name='handover_spiel',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lynkcapital',
            name='received_a_letter_spiel',
            field=models.TextField(blank=True, null=True),
        ),
    ]
