# Generated by Django 3.1.1 on 2022-07-12 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20220712_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrequest',
            name='area_of_specialization',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost'),
        ),
    ]