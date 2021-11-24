from django import forms
from django.forms import models, widgets
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(forms.Form):
    COUNTRIES = (
        (0, 'Albania'),
        (1, 'Andorra'),
        (2, 'Austria'),
        (3, 'Azerbaijan'),
        (4, 'Belarus'),
        (5, 'Belgium (FR)'),
        (6, 'Bulgaria'),
        (7, 'Croatia'),
        (8, 'Denmark'),
        (9, 'Deutschland'),
        (10, 'Estonia')
    )
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label='Phone Number')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Password Confirmation', widget = forms.PasswordInput)
    adress = forms.CharField(label="Adress")
    second_adress = forms.CharField(label="Second Adress")
    country = forms.CharField(label="Country")
    town = forms.CharField(label="Town or City")
    
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation does not match.')
        email = data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already in use')
        return data    



class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data['email']).first()
        if not user:
            raise forms.ValidationError('User does not exist')
        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError('Password is incorrect')
        return self.cleaned_data

    