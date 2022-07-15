from distutils.log import FATAL
from django.shortcuts import render, redirect
from . forms import SignUpForm, UserUpdateForm, EmployeeProfileUpdateForm, EmployerProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here. 

def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('homepage')
    else:
        user_form = SignUpForm()
        
    context = {
        'user_form': user_form,
        
    }
    return render(request, 'users/signup.html', context)

@login_required(login_url='login')
def profile(request):
    
    return render(request, 'users/profile.html')

@login_required(login_url='login')
def employee_update_profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        employee_profile_update_form = EmployeeProfileUpdateForm(request.POST, request.FILES, instance = request.user.user_profile)
        employer_profile_update_form = EmployerProfileUpdateForm(request.POST, request.FILES, instance = request.user.user_profile)
        if user_update_form.is_valid() and employee_profile_update_form.is_valid():
            user_update_form.save()
            employee_profile_update_form.save()
            messages.success(request, 'Successfully updated Profile')
            return redirect('user_profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        employee_profile_update_form = EmployeeProfileUpdateForm(instance=request.user.user_profile)
        employer_profile_update_form = EmployerProfileUpdateForm(instance = request.user.user_profile)
       
    context = {
        'user_update_form': user_update_form,
        'employee_profile_update_form': employee_profile_update_form,
        'employer_profile_update_form': employer_profile_update_form
    }
    return render(request, 'users/profile_update.html', context)

