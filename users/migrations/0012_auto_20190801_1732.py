# Generated by Django 2.1.2 on 2019-08-01 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_changed_to_list_of_staffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='assigned_pm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_managers', to='fillables.ProjectManager', verbose_name='Assigned PM'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='assigned_va',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='virtual_assistants', to='fillables.VirtualAssistant', verbose_name='Assigned VA'),
        ),
    ]
