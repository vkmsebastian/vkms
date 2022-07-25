from django.urls import path

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('', views.index, name='home'),
]