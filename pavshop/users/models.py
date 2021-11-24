from django.db import models
from django.forms import widgets
from pavshop.utils.base import BaseModel
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField


class Country(BaseModel):
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
    name = models.IntegerField(choices=COUNTRIES, default=0, verbose_name="Name of the Designer")
    
    def __str__(self) -> str:
        return f'self.name'


class User(AbstractUser):
    email = models.EmailField(unique=True, default="")
    phone = models.CharField(max_length=255, verbose_name="Phone Number",default="")
    adress = models.CharField(max_length=255, verbose_name="Address",default="")
    second_adress = models.CharField(max_length=255, verbose_name="Second Adress",default="")
    # country = models.ForeignKey('users.Country', related_name="Country", on_delete=models.CASCADE, verbose_name="Country", default="", null=True, blank=True)
    country = models.CharField(max_length=255)
    town = models.CharField(max_length=255, verbose_name="Town or City",default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



