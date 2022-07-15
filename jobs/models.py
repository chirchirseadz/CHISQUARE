from statistics import mode
from tkinter.messagebox import NO
from django.db import models
from users.models import user_profile
# Create your models here.

class JobPost(models.Model):

    PROFFESION = (
        ('IT specialist', 'IT specialist'),
        ('Administative Assistant','Administrative Assistant'),
        ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'),
        ('Hospitality','Hospitality'),
        ('Customer Care','Customer Care'),
        ('Hospitality And Wait Staff','Hospitality And Wait Staff'),
        
    )
    employer = models.OneToOneField(user_profile, on_delete=models.CASCADE, null =True)
    area_of_specialization = models.CharField(max_length=100, choices= PROFFESION, null=True)
    title = models.CharField(max_length=100,null=True)
    job_desc =  models.TextField(blank=True)
    budget =  models.FloatField()
    date_posted = models.DateTimeField(auto_now_add=True)
    terms_and_conditions = models.BooleanField(default=False)
    job_taken = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.area_of_specialization}'
    
class jobrequest(models.Model):
    TERMS_OF_SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Permanent','Permanent'),
        

    )
    user_requesting = models.OneToOneField(user_profile, on_delete=models.CASCADE, null=True)
    area_of_specialization = models.OneToOneField(JobPost, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100,null=True)
    proposal = models.TextField(blank=True)
    terms_of_service = models.CharField(max_length=100, choices=TERMS_OF_SERVICE, null=True)
    your_budget = models.FloatField()
    terms_and_conditions = models.BooleanField(default=False)
    
       
        
    def __str__(self):
            return f'{self.title}'

class FindTalentRequest(models.Model):
    PROFFESION = (
        ('IT specialist', 'IT specialist'),
        ('Administative Assistant','Administrative Assistant'),
        ('Clerical And Data Entry Personel ', 'Clerical And Data Entry Personel'),
        ('Hospitality','Hospitality'),
        ('Customer Care','Customer Care'),
        ('Hospitality And Wait Staff','Hospitality And Wait Staff'),
        
    )
    
    LOCATION = (
        ('Nairobi','Nairobi'),
        ('Kisumu','Kisumu'),
        ('Mombasa','Mombasa'),
        ('nakuru','Nairobi'),
        
    )
    SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Parmanent','Parmanent'),
    )
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    area_of_specialization = models.CharField(max_length=100, choices= PROFFESION, null=True)
    job_title = models.CharField(max_length=100, null =True)
    your_info = models.TextField(blank=True)
    location = models.CharField(max_length=100, choices=LOCATION, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    terms_of_service =  models.CharField(max_length=100, choices=SERVICE, null=True)
    date_of_request = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title

# skills_experience
# job_experience
# budget
# date_posted

