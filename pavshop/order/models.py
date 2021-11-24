from django.db import models
from django.forms import widgets

from pavshop.utils.base import BaseModel

class Checkout_billing(BaseModel):
    
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    town = models.CharField(max_length=255, verbose_name="Town")
    country = models.CharField(max_length=255, verbose_name="Country")
    email = models.EmailField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    user = models.OneToOneField('users.User', related_name="billingAdress", on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)

    class Meta:
        verbose_name = "Checkout_billing"
        verbose_name_plural = "Checkout_billings"

    def __str__(self) -> str:
        return self.first_name



class Shipping_Info(BaseModel):
    PAYMENT_METHOD = (
        (1, "Direct bank transfer"),
        (2, "Cash on delivery"),
        (3, "Cheque payment"),
        (4, "Paypal")
    )
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    town = models.CharField(max_length=255, verbose_name="Town")
    country = models.CharField(max_length=255, verbose_name="Country")
    email = models.EmailField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    user = models.ForeignKey('users.User', related_name="shippingAdress", on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
    is_main = models.BooleanField(verbose_name="Is Main?", default=False)
    payment = models.IntegerField(default=1, verbose_name="Payment")

    class Meta:
        verbose_name = "Shipping_Info"
        verbose_name_plural = "Shipping_Infos"


    def __str__(self) -> str:
        return self.first_name



class Payment_method(BaseModel):
    PAYMENT_METHOD = (
        (1, "Direct bank transfer"),
        (2, "Cash on delivery"),
        (3, "Cheque payment"),
        (4, "Paypal")
    )
    payment = models.IntegerField(default=1, verbose_name="Payment")

    class Meta:
        verbose_name = "Payment_method"
        verbose_name_plural = "Payment_methods"

    def __str__(self):
        return f'self.payment'


    
