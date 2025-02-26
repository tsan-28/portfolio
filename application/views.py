from django.template import loader
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from App import settings
from django.core.mail import EmailMessage
from .models import (
    Profile,
    Project,
    Contact,
    Education,
    Experience,
    Expert,
    Referee
)
from .forms import (
    LoginForm,
    profile_updateForm,
    EmailForm,
    
)






#this is the home page view
def home_view(request):
    contacts = Contact.objects.all()
    person = User.objects.all()
    projects = Project.objects.all()
    template = loader.get_template('accounts/home_page.html')

    context = {
        'person': person,
        'projects': projects,
        'contacts': contacts
    }
    return HttpResponse(template.render(context, request))





#this is the login page view
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                failed_attempts = cache.delete(f'failed_logins_{username}')
                return redirect('/')
            else:
                failed_attempts = cache.get(f'failed_logins_{username}', 0) + 1
                cache.set(f'failed_logins_{username}', failed_attempts, timeout=300)
                if failed_attempts >= settings.LOGIN_ATTEMPT_LIMIT:
                    messages.error(request, 'Too many failed attempts. Please try again later.')
                else:
                    messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login_page.html', {'form': form})




#this is the view for registering new members
def register_view(request):
    template =loader.get_template('accounts/register_page.html')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        user_obj = User.objects.filter(username=username)   
        if user_obj.exists():
            messages.error(request, "Username already taken")

        else:
            user = User.objects.create(
                username=username,
                email=email,
                password = password1
            )
            user.save()
            login(request, user)
            messages.success(request, "User created successfully")
            return redirect('/')
    return HttpResponse(template.render(context, request))





#this view logs out a user and redirects them to the home page
def log_out_view(request):
    logout(request)
    return redirect('home')
        




@login_required(login_url="/login")
def profiles_list_view(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, 'accounts/profiles_page.html', context)




def send_email(request):  # Rename the view function to avoid conflict
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)  # Use EmailForm here
        if form.is_valid():
            recipient = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            attachment = form.cleaned_data['attachment']
            message = form.cleaned_data['description']
            
            # Create EmailMessage instance
            email = EmailMessage(subject, message, to=[recipient])
            email.attach(attachment.name, attachment.read(), attachment.content_type)
            email.send()
            
            return redirect('emailsuccess')  # Redirect after a successful email send
    else:
        form = EmailForm()  # Instantiate the form correctly here
    
    return render(request, 'email/send_email.html', {'form': form})


def emailConfirm_view(request):
    return render(request, 'email/email_success.html')

def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
        else:
            messages.error(request, "Input valid password")
    return render(request, 'accounts/change_password.html', {'form': form})





def profile_details_view(request, slug):
    try:
        # Fetch the profile or return a 404 if it doesn't exist
        profile = get_object_or_404(Profile, slug=slug)

        # Fetch education records associated with the profile's user
        education = Education.objects.filter(user=profile.user)
        experience = Experience.objects.filter(user=profile.user)
        referee = Referee.objects.filter(user=profile.user)

        # Pass the profile and education to the template
        context = {
            'profile': profile,
            'education': education,
            'experience': experience,
            'referre': referee,
        }
        return render(request, 'accounts/profile_details.html', context)

    except Exception as e:
        return render(request, 'accounts/error.html', {'error': str(e)})
    




def update_profile(request, slug):
    obj = get_object_or_404(Profile, slug=slug)
    form = profile_updateForm(instance=obj)
    context = {"form": form}
    return render(request, 'accounts/edit_profile.html', context)


def project_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        
        }
    return render(request, 'project/projects_page.html', context)
