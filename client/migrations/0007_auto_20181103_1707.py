# Generated by Django 2.1.2 on 2018-11-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20181103_1658'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='StatusChoice',
        ),
        migrations.RenameField(
            model_name='statuschoice',
            old_name='status_choices',
            new_name='status',
        ),
    ]
