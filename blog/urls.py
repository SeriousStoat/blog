from django.urls import path
from . import views

urlpatterns = [
    path("about", views.blog_about, name="blog_about"),
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("search/", views.search_feature, name="search-view")
]