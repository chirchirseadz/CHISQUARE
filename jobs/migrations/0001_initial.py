# Generated by Django 3.2.9 on 2022-07-26 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindTalentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('area_of_specialization', models.CharField(choices=[('IT specialist', 'IT specialist'), ('Administative Assistant', 'Administrative Assistant'), ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'), ('Hospitality', 'Hospitality'), ('Customer Care', 'Customer Care'), ('Hospitality And Wait Staff', 'Hospitality And Wait Staff')], max_length=100, null=True)),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('your_info', models.TextField(blank=True)),
                ('location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Mombasa', 'Mombasa'), ('nakuru', 'Nairobi')], max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
                ('terms_of_service', models.CharField(choices=[('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Parmanent', 'Parmanent')], max_length=100, null=True)),
                ('date_of_request', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_of_specialization', models.CharField(choices=[('IT specialist', 'IT specialist'), ('Administative Assistant', 'Administrative Assistant'), ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'), ('Hospitality', 'Hospitality'), ('Customer Care', 'Customer Care'), ('Hospitality And Wait Staff', 'Hospitality And Wait Staff')], max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('job_desc', models.TextField(blank=True)),
                ('budget', models.FloatField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('terms_and_conditions', models.BooleanField(default=False)),
                ('job_taken', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('employer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='jobrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('proposal', models.TextField(blank=True)),
                ('terms_of_service', models.CharField(choices=[('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=100, null=True)),
                ('your_budget', models.FloatField()),
                ('terms_and_conditions', models.BooleanField(default=False)),
                ('area_of_specialization', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost')),
                ('user_requesting', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user_profile')),
            ],
        ),
    ]
