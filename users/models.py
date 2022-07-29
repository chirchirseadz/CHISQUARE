from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
    PROFFESION = (
        ('IT specialist', 'IT specialist'),
        ('Administrative Assistant','Administrative Assistant'),
        ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'),
        ('Hospitality','Hospitality'),
        ('Customer Care','Customer Care'),
        ('Hospitality And Wait Staff','Hospitality And Wait Staff'),
       
    )
    EXPERIENCE = (
         ('0-3 Years','0-3 Years'),
         ('4-6 Years','4-6 Years'),
         ('7-10 Years','7-10 Years'),
         ('11+ Years',' 11+ Years'),
    )
    COUNTY = (
       ('Nairobi','Nairobi'),
       ('kisumu','kisumu'),
       ('Uasin-gishu','Uasin-gishu'),
       ('kwale','kwale'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="user")
    national_id = models.PositiveIntegerField(null=True, unique=True, verbose_name='National Id')
    area_of_specialization = models.CharField(max_length=100, choices= PROFFESION, null=True)
    job_title = models.CharField(max_length=100, null=True)
    brief_info = models.TextField(blank=True, verbose_name='Brief Description', null=True)
    address = models.CharField(max_length=255, verbose_name='Location Address', null=True)
    phone  = models.CharField(max_length=20, verbose_name='Mobile Phone Number', null=True)
    current_location = models.CharField(max_length=20, choices=COUNTY)
    company_name = models.CharField(max_length=100, null=True)
    company_email = models.EmailField(null=True)
    image  = models.ImageField(default='empty.jpg', upload_to='images/', verbose_name='Profile picture', null=True) 
    profile_updated = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username




