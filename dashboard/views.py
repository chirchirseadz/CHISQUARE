from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import user_profile
from jobs.forms import FindTalentRequestForm
from jobs.models import JobPost
from django.contrib.auth.models import User
from jobs.models import FindTalentRequest


# Create your views here.

    

def landing_page(request):
    data = FindTalentRequest.objects.all()
    context = {
        'data':data
    }
    
    return render(request, 'dashboard/landing_page.html', context)



@login_required(login_url='login')
def index(request):
    return render(request, 'dashboard/index.html')

def about(request):
    return render(request, 'dashboard/about.html')


def blog(request):
    return render(request, 'dashboard/blog.html')



def contact(request):
    return render(request, 'dashboard/contact.html')


    
################### talent works ###########

def admin_assistant(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'dashboard/admin_assistant.html',context)

def clerk_data_entry(request):
    return render(request, 'dashboard/clerk_data_entry.html')


def it_spacialist(request):
    return render(request, 'dashboard/it_spacialist.html')

def hospitality(request):
    return render(request, 'dashboard/hospitality.html')


def customer_care(request):
    return render(request, 'dashboard/customer_care.html')

def hospitality_wait_staff(request):
    return render(request, 'dashboard/hospitality_wait_staff.html')

def testimolnials(request):
    return render(request, 'dashboard/testimonials.html')
