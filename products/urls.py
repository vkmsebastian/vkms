from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/update/', views.update, name="products_update"),
    path('<int:id>/delete/', views.delete, name="products_delete"),
    path('<int:id>/edit/', views.index, name="products_edit"),
    path('', views.index, name='products_index'),
]