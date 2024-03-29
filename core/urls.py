"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings

from django.conf import settings
from django.conf.urls.static import static


from users import views as user_views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # administartion 
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('jobs/', include('jobs.urls')),

    # users authentications 
    path('krn/skr/admin/reg/', user_views.admin_signup, name='admin_signup'),
    path('employer/signup/', user_views.employer_signup, name='employer_signup'),
    path('employee/signup/', user_views.employee_signup, name='employee_signup'),
    path('login/', auth_views.LoginView.as_view(template_name = ('users/login.html')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = ('users/logout.html')), name='logout'),

    # users reset password 

    # profile section

    path('profile/', user_views.profile, name='user_profile'),
    path('employer_profile_update/',user_views.employer_profile_update, name='employer_profile_update'),
    path('update_profile/', user_views.profile_update, name='update_profile'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
