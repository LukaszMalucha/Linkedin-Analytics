from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from core import models
from .forms import UserLoginForm, UserRegistrationForm, MyProfileForm


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(email=request.POST['email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('/')
            else:
                messages.error(request, "Incorrect username or password")
    else:
        login_form = UserLoginForm()

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('/')

            else:
                messages.error(request, "Unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('/')


@login_required
def profile(request):
    my_profile = get_object_or_404(models.MyProfile, owner=request.user)

    context = {'user': request.user, 'my_profile': my_profile}

    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    my_profile = get_object_or_404(models.MyProfile, owner=request.user)
    my_details_form = MyProfileForm(request.POST, request.FILES, instance=my_profile)
    if request.method == 'POST':
        if my_details_form.is_valid():
            my_profile.save()

            return redirect(reverse('user:profile'))

    return render(request, 'edit_profile.html', {'my_profile': my_profile, 'my_details_form': my_details_form})
