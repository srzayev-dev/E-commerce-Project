from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"), 
    path("shoppingcart/", views.shopping_cart, name="shopping_cart"),
]