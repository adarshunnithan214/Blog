from django.urls import path
from .views import create_blog, blog_list, blog_detail, edit_blog, delete_blog

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', create_blog, name='create_blog'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', edit_blog, name='edit_blog'),
    path('<int:pk>/delete/', delete_blog, name='delete_blog'),
]
