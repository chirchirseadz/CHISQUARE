# Generated by Django 3.2.9 on 2023-01-04 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobrequest_job_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobrequest',
            old_name='job_category',
            new_name='job_name',
        ),
    ]
