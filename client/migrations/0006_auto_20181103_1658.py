# Generated by Django 2.1.2 on 2018-11-03 08:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20181103_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status_choices', models.CharField(default='Active', max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.Status'),
        ),
    ]