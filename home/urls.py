"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('blog_view', views.blog_view, name='blog_view'),
    path('blog_post/<int:pk>/', views.blog_post, name='blog_post'),
    path('my_blogs', views.my_blogs, name='my_blogs'),
    path('edit_blog/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('search_blogs', views.blog_view_search, name='search_blogs')
]