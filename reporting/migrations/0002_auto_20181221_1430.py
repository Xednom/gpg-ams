# Generated by Django 2.1.2 on 2018-12-21 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vatimesheet',
            name='clients_full_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.CompanyName'),
        ),
        migrations.AlterField(
            model_name='vatimesheet',
            name='date_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.DateInformation'),
        ),
        migrations.AlterField(
            model_name='vatimesheet',
            name='list_of_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.Task'),
        ),
        migrations.AlterField(
            model_name='vatimesheet',
            name='project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.ProjectManager'),
        ),
        migrations.DeleteModel(
            name='DateInformation',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
