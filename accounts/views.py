from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, CustomPasswordChangeForm
from accounts.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home:index')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('accounts:login')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:edit_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed.')
            return redirect('accounts:edit_profile')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'profile_user': user})


@login_required
def order_history(request):
    orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'accounts/order_history.html', {'orders': orders})


@login_required
def wishlist(request):
    wishlist_items = request.user.wishlist.all()
    return render(request, 'accounts/wishlist.html', {'wishlist_items': wishlist_items})