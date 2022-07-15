from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import user_profile
from jobs.forms import FindTalentRequestForm


# Create your views here.

    

def landing_page(request):
    return render(request, 'dashboard/landing_page.html', )



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
    admin_assistant = user_profile.objects.filter('Administrative Assistant')
    context = {
        admin_assistant
    }
    return render(request, 'dashboard/admin_assistant.html')

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
