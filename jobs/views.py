from re import template
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostJobForm, JobProposalForm, FindTalentRequestForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string




# Create your views here.
# page request 

def jobrequest(request):
    if request.method == 'POST':
        request_form = FindTalentRequestForm(request.POST)
        if request_form.is_valid():
            request_form.save()
            first_name = request_form.cleaned_data.get('first_name')
            email = request_form.cleaned_data.get('email')
            template = render_to_string('emails/email_request.html', {'name': first_name})
            email_message = EmailMessage(
            'Message from the Admin', # here we have the subject
                template, # here is the boy message ):
                settings.EMAIL_HOST_USER, # This is the sender
                [email,] # This is the recepient 
            )
            email_message.fail_silently = False
            email_message.send()
            request_form.save()
            return redirect('landing_page')

                  
            
    else:
        request_form = FindTalentRequestForm()
    context = {
        'request_form': request_form
    }
    return render(request, 'jobs/jobrequest.html', context)




# end


@login_required(login_url='user-login')
def post_job(request):
    if request.method == 'POST':
        post_job = PostJobForm(request.POST)
        if post_job.is_valid(): 
            post_job.save(commit=False)
            terms_and_conditons = post_job.cleaned_data['terms_and_conditions']
            if  terms_and_conditons == False:
                return redirect('postjobs_terms_errors')
            else:
                post_job.save()
                messages.success(request, 'Has been posted Successfully')
                return redirect('homepage')
    else:
        post_job = PostJobForm()
    context = {
        'post_job': post_job
    }
    return render(request, 'jobs/postjob.html', context)


@login_required(login_url='user-login')
def postjobs_terms_errors(request):
    return render(request, 'errors/postjob_terms_error.html')

############################################################

@login_required(login_url='user-login')
def proposal(request):
    if request.method == 'POST':
        proposal = JobProposalForm(request.POST)
        if proposal.is_valid():
            proposal.save(commit=False)
            terms_and_conditions = proposal.cleaned_data['terms_and_conditions']
            if terms_and_conditions == False:
                return redirect('proposal_terms_errors')
            else: 
                proposal.save()
                return redirect('homepage')
     
    else:
        proposal = JobProposalForm()
    context = {
        'proposal': proposal
        }
            
    return render(request,'jobs/proposal.html', context)

@login_required(login_url='user-login')
def proposal_terms_errors(request):
    return render(request, 'errors/postjob_terms_error.html')

