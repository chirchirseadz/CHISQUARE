# Generated by Django 3.2.9 on 2023-01-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField()),
                ('date_message', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
