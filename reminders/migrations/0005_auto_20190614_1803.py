# Generated by Django 2.1.2 on 2019-06-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0004_auto_20190614_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managerreminders',
            old_name='additional_comment_requestee_client',
            new_name='additional_comment',
        ),
        migrations.RemoveField(
            model_name='managerreminders',
            name='additional_comment_requestee_staff',
        ),
    ]
