from dataclasses import fields
from . models import JobPost, jobrequest, FindTalentRequest, HireTalentRequest
from django import forms


class PostJobForm(forms.ModelForm):
    class Meta:
        terms_and_conditions = forms.BooleanField( required=True, disabled=True)
        model = JobPost
        fields = ['area_of_specialization','title','job_desc','budget','terms_and_conditions']
        
        labels = {
            'title': 'Job title',
            'job_desc': 'Describe Your The job you want to post. Ensure you have captured every detail',
            'budget': 'Budget in (ksh)'
        }

    
    
        


class JobProposalForm(forms.ModelForm):
    class Meta:
        model = jobrequest
        fields = ['area_of_specialization','title','proposal', 'your_budget','terms_and_conditions']
    
        labels = {
            'your_budget': 'Your Budget in (ksh)'
        }

class FindTalentRequestForm(forms.ModelForm):
    class Meta:
        model = FindTalentRequest
        fields = ['first_name','last_name','email', 'area_of_specialization','job_title','your_info','location', 'phone_number','terms_of_service',]


class HireTalentRequestForm(forms.ModelForm):
    class Meta:
        model = HireTalentRequest
        fields = ['first_name', 'last_name', 'email','area_of_need','your_specifications','phone_number','location','terms_of_service']