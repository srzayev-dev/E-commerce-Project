from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("blog/list/", views.blogList.as_view(), name="blog_list"), 
    path("blog/detail/<int:pk>/", views.BlogGenericDetail.as_view(), name="blog_detail"),
    path("blog/january-archive/", views.januar_blogs, name="january_blogs"),
    path("blog/february-archive/", views.februar_blogs, name="february_blogs"),
    path("blog/march-archive/", views.martch_blogs, name="march_blogs"),
    path("blog/april-archive/", views.april_blogs, name="april_blogs"),
    path("blog/may-archive/", views.may_blogs, name="may_blogs"),
    path("blog/june-archive/", views.june_blogs, name="june_blogs"),
    path("blog/july-archive/", views.july_blogs, name="july_blogs"),
    path("blog/august-archive/", views.august_blogs, name="august_blogs"),
    path("blog/september-archive/", views.september_blogs, name="september_blogs"),
    path("blog/october-archive/", views.october_blogs, name="october_blogs"),
    path("blog/november-archive/", views.november_blogs, name="november_blogs"),
    path("blog/december-archive/", views.december_blogs, name="december_blogs"),
    path("blog/search-blog/", views.search_method, name="search_blog"),
]
