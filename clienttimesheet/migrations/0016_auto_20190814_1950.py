# Generated by Django 2.1.2 on 2019-08-14 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clienttimesheet', '0015_auto_20190814_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='assigned_approval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Staffs'),
        ),
    ]
