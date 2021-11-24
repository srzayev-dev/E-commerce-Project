from django.contrib.auth import get_user_model, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import request
from django.shortcuts import render,redirect
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib import auth, messages
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required




User = get_user_model()

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data.get('email')).first()
            login(request,user)
            return redirect('home')
        print(form.errors)
        return redirect('login')
    else:
        form = UserLoginForm()


    return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username = form.cleaned_data.get('email'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                phone = form.cleaned_data.get('phone'), 
                adress = form.cleaned_data.get('adress'),
                second_adress = form.cleaned_data.get('second_adress'),
                country = form.cleaned_data.get('country'),
                town = form.cleaned_data.get('town')
                    
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context=context)


def logout_view(request):
    auth.logout(request)
    return redirect('home')

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form':form})
