from django.contrib import admin
from django.urls import path
from . import views 
from django.views.generic.base import RedirectView
from .views import HomeView, aboutView, blog_list, blog_detail, resource_detail, resource_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HomeView.as_view(),name='home'),
    path('about/',views.aboutView.as_view(),name='about'),

    path('blog/',views.blog_list, name = 'blog-list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),   
    
    path('resource/',views.resource_list, name = 'resource-list'),
    path('resource/<int:pk>/', views.resource_detail, name='resource-detail'),

    path('',RedirectView.as_view(url="home/")),
]