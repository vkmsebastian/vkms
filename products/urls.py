from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/edit/', views.index, name="edit"),
    path('', views.index, name='index'),
]