from django.shortcuts import render, redirect


from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            messages.success(request, f'Account created for Successfully')
            return redirect('sign-in')
        else:
             forms = UserRegisterForm()
    else:
        forms = UserRegisterForm()
    return render(request, 'users/register.html', {'forms': forms})



def signin(request):
    if request.user.is_authenticated: #checks if user is authenticated and redirects back to home page
        messages.warning(request, 'You are logged in Already')
        return redirect('home')
    
    if request.method == 'POST': #checks if the request is a POST request
        email = request.POST.get('email')  #gets the user email from the login input fields
        password = request.POST.get('password')  #gets the user password from the login input fields

        try: # Use try and catch exceptions to check if the user has an account registered
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None: # if the user exist
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect('home')
            else: #if the user does not exist
                messages.warning(request, 'User does not Exist, Create an account')
        except:
            messages.warning(request, f"User with {email} does not exist")
        

    return render(request, 'users/sign-in.html')




def sign_out(request):
    logout(request)
    messages.success(request, f" You are logged out")

    return redirect('sign-in')


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile after saving
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/edit-profile.html', {'form': form})