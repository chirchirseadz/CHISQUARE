# Generated by Django 3.1.1 on 2022-07-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20220713_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findtalentrequest',
            name='area_of_specialization',
            field=models.CharField(choices=[('IT specialist', 'IT specialist'), ('Administative Assistant', 'Administrative Assistant'), ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'), ('Hospitality', 'Hospitality'), ('Customer Care', 'Customer Care'), ('Hospitality And Wait Staff', 'Hospitality And Wait Staff')], max_length=100, null=True),
        ),
    ]
