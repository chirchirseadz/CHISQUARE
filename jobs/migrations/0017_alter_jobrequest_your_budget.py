# Generated by Django 3.2.9 on 2023-01-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_job_company_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='your_budget',
            field=models.FloatField(null=True),
        ),
    ]
