# Generated by Django 3.2.9 on 2023-01-04 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_area_of_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.areaofspecialization'),
        ),
    ]
