# Generated by Django 2.1.2 on 2019-06-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_channelofcommunications_notesaftertraining'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channelofcommunications',
            options={'verbose_name': 'Channel of Communication', 'verbose_name_plural': 'Channel of Communications'},
        ),
        migrations.AddField(
            model_name='staffs',
            name='category',
            field=models.CharField(blank=True, choices=[('Office Based', 'Office Based'), ('Part-timers', 'Part-timers'), ('Home Based', 'Home Based'), ('Freelance', 'Freelance')], max_length=150, null=True),
        ),
    ]
