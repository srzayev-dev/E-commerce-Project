from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name = "product_detail"),
    path("product_list/", views.ProductListView.as_view(), name = "product_list"),
]