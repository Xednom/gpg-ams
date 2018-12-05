# Generated by Django 2.1.2 on 2018-12-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobrequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='status',
            field=models.CharField(choices=[('----', '------'), ('complete', 'Complete'), ('in-progress', 'In Progress'), ('for-final-review', 'For Final Review'), ('job-request-sent-to-va', 'Job Request Sent to VA')], default='----', max_length=100),
        ),
    ]
