from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path("", views.home_view, name = "home"),
    path("contact/", views.ContactFormView.as_view(), name = "contact"),
    path("about_us/", views.AboutUs.as_view(), name = "about_us"),
    path("profile/", views.profile_view, name = "profile"),
    path("search_products/", views.search_view, name = "search-product"),
    path("set_language/", views.change_lang, name = "set_language"),

]
