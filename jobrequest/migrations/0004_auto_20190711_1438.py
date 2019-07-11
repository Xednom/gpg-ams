# Generated by Django 2.1.2 on 2019-07-11 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobrequest', '0003_auto_20190711_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='assigned_project_managers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PMs', to='users.Staffs'),
        ),
        migrations.AlterField(
            model_name='jobrequest',
            name='assigned_va',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='VAs', to='users.Staffs'),
        ),
    ]
