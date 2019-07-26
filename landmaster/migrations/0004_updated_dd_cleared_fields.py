# Generated by Django 2.1.2 on 2019-07-23 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0003_auto_20190717_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duediligencescleared',
            old_name='notes',
            new_name='additional_memo',
        ),
        migrations.RenameField(
            model_name='duediligencescleared',
            old_name='operators_details',
            new_name='call_details',
        ),
        migrations.RenameField(
            model_name='duediligencescleared',
            old_name='total_hours',
            new_name='total_minutes',
        ),
        migrations.RemoveField(
            model_name='duediligencescleared',
            name='call_in',
        ),
        migrations.RemoveField(
            model_name='duediligencescleared',
            name='call_out',
        ),
        migrations.RemoveField(
            model_name='duediligencescleared',
            name='client_company_name',
        ),
        migrations.RemoveField(
            model_name='duediligencescleared',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='duediligencescleared',
            name='contact_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligencescleared',
            name='customer_representative_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligencescleared',
            name='operator_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligencescleared',
            name='questions_requested_to_ask',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligencescleared',
            name='reason_of_the_call',
            field=models.TextField(blank=True, null=True, verbose_name='Reason(s) of the call'),
        ),
        migrations.AlterField(
            model_name='duediligencescleared',
            name='apn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duediligencescleared',
            name='client_full_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Clients'),
        ),
        migrations.AlterField(
            model_name='duediligencescleared',
            name='customer_service_representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Staffs'),
        ),
        migrations.AlterField(
            model_name='duediligencescleared',
            name='department_calling_about',
            field=models.TextField(blank=True, null=True),
        ),
    ]