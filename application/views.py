from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
)



#this is the home page view
def home_view(request):
    contacts = Contact.objects.all()
    person = User.objects.all()
    projects = Project.objects.all()
    template = loader.get_template('home_page.html')

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
                return redirect('/')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'login_page.html', {'form': form})

#this is the view for registering new members
def register_view(request):
    template =loader.get_template('register_page.html')
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
    return render(request, 'profiles_page.html', context)




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
        return render(request, 'profile_details.html', context)

    except Exception as e:
        # Handle any unexpected errors
        return render(request, 'error.html', {'error': str(e)})
    

def update_profile(request, slug):
    obj = Profile.objects.get_object_or_404(slug=slug)
    form = profile_updateForm(instance=obj)
    context = {"form": form}
    return render(request, 'edit_profile.html', context)
