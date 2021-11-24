from django import forms
from django.db.models import fields
from django.forms import widgets
from order.models import Checkout_billing, Shipping_Info, Payment_method


class billing_form(forms.ModelForm):
    class Meta:
        model = Checkout_billing
        fields = '__all__'


    def clean(self):
        data = self.cleaned_data.get('first_name')
        if len(data) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return self.cleaned_data



class shipping_form(forms.ModelForm):
    PAYMENT_METHOD = (
        (1, "Direct bank transfer"),
        (2, "Cash on delivery"),
        (3, "Cheque payment"),
        (4, "Paypal")
    )
    payment = forms.ChoiceField(choices=PAYMENT_METHOD, widget=forms.RadioSelect(attrs={'class' : 'form-check-input'}))
    class Meta:
        model = Shipping_Info
        fields = '__all__'

    
class place_order_form(forms.ModelForm):
    PAYMENT_METHOD = (
        (1, "Direct bank transfer"),
        (2, "Cash on delivery"),
        (3, "Cheque payment"),
        (4, "Paypal")
    )
    payment = forms.ChoiceField(choices=PAYMENT_METHOD, widget=forms.RadioSelect(attrs={'class' : 'form-check-input'}))
    class Meta:
        model = Payment_method
        fields = ['payment']
        
