# Generated by Django 3.1.1 on 2022-07-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_jobrequest_date_of_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobrequest',
            name='date_of_request',
        ),
        migrations.AddField(
            model_name='findtalentrequest',
            name='date_of_request',
            field=models.DateTimeField(auto_now=True),
        ),
    ]