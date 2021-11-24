from django import forms
from core.models import Subscribe , Contact_us
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ["fullname", "email",'phone','subject' ,"message"]


    
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))
    
    def clean_field(self):
        data = self.cleaned_data["fullname"]
        if len(data) <= 3:
            raise forms.ValidationError("4-den az herf ola bilmez")
        return data



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        widgets = {
            'email' : widgets.EmailInput(attrs={'class': 'input-text required-entry validate-email', 'placeholder': 'Enter your email address'} ),
        }
    def clean_email(self):
        mail = self.cleaned_data.get('mail')
        if Subscribe.objects.filter(mail=mail).exists():
            raise forms.ValidationError("Email already in use")
        return mail
    

# class SearchForm(forms.Form):
#     search = forms.CharField(max_length=255)