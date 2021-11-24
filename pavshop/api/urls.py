from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from . import views



from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# router = DefaultRouter()
# router.register(r'register', views.UserViewSet)

product_patterns = [
    path('', views.ProductAPIView.as_view(), name='products'),
    path('<int:pk>/', views.ProductAPIView.as_view(), name='products_detail'),
    path('<product_id>/versions/', views.ProductVersionAPIView.as_view(), name='product_versions'),
    path('<product_id>/versions/<int:pk>/', views.ProductVersionAPIView.as_view(), name='product_version_detail'),
]

auth_views = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

registration_views = [
    path('register_api/', views.CreateUserView.as_view(), name='register_api'),

]

urlpatterns = [
    path("blogs/", views.ListBlogAPIView.as_view(), name="blogs_list"),
    path("blog_create/", views.CreateBlogAPIView.as_view(), name="create_blog"),
    path("blog_update/<int:pk>/", views.UpdateBlogAPIView.as_view(), name="update_blog"),
    path("blog_delete/<int:pk>/", views.DeleteBlogAPIView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/", views.SingleBlogAPIView.as_view(), name="single_blog"),
    path("b_c_list/", views.ListBlogCategoryAPIView.as_view(), name="blog_category_list"),
    path("b_c_create/", views.CreateBlogCategoryAPIView.as_view(), name="blog_category_create"),
    path("b_c_update/<int:pk>/", views.UpdateBlogCategoryAPIView.as_view(), name="blog_category_update"),
    path("b_c_delete/<int:pk>/", views.DeleteBlogCategoryAPIView.as_view(), name="blog_category_delete"),
    path("p_c_list/", views.ListProductCategoryAPIView.as_view(), name="product_category_list"),
    path("p_c_create/", views.CreateProductCategoryAPIView.as_view(), name="product_category_create"),
    path("p_c_update/<int:pk>/", views.UpdateProductCategoryAPIView.as_view(), name="product_category_update"),
    path("p_c_delete/<int:pk>/", views.DeleteProductCategoryAPIView.as_view(), name="product_category_delete"),
    path("api_login/", views.LoginAPI.as_view(), name="api_login"),
    path('products/', include(product_patterns)),
    path('', include(auth_views)),
    path('', include(registration_views)),
    path('card/', views.CardView.as_view(), name='card'),
    path('itemCard/', views.ItemCardView.as_view(), name='cardItem'),
    path('subscribe/', views.SubscriberAPIView.as_view(), name='subscribe'),
]