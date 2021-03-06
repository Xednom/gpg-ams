# Generated by Django 2.1.2 on 2019-06-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('fillables', '0001_initial'),
        ('landmaster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duediligence',
            name='dd_va_assigned_call_outs_other_requests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='other', to='users.Staffs', verbose_name='VA - Other Requests'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='dd_va_assigned_call_outs_tax_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tax', to='users.Staffs', verbose_name='VA - Tax Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='dd_va_assigned_call_outs_utilities_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='utilities', to='users.Staffs', verbose_name='VA - Utilities Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='dd_va_assigned_call_outs_zoning_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='zoning', to='users.Staffs', verbose_name='VA - Zoning Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='dd_va_assigned_initial_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='initial', to='users.Staffs', verbose_name='VA - Initial Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.ProjectManager'),
        ),
    ]
