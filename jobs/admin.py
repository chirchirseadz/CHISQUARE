from django.contrib import admin
from .models import JobPost, jobrequest, FindTalentRequest

# Register your models here.

class JobPostAdmin(admin.ModelAdmin):
    list_display = ['area_of_specialization','title','job_desc','budget','terms_and_conditions']
    list_filter = ['area_of_specialization']

admin.site.register(JobPost, JobPostAdmin)



class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title','proposal', 'your_budget','terms_and_conditions']
admin.site.register(jobrequest, ProposalAdmin)

class FindTalentRequestAdmin(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','area_of_specialization','job_title','location','phone_number','terms_of_service','date_of_request']
    list_filter = ['date_of_request','area_of_specialization',]
admin.site.register(FindTalentRequest, FindTalentRequestAdmin )