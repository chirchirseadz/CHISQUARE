# Generated by Django 3.1.1 on 2022-07-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20220712_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='findtalentrequest',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='findtalentrequest',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]