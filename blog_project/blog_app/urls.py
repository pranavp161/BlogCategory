from django.urls import path
from .views import blog_create, blog_list

urlpatterns = [
    path('create/', blog_create, name='blog_create'),  
    path('', blog_list, name='blog_list'),
]