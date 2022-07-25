from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/update/<int:page>', views.update, name="products_update"),
    path('<int:id>/delete/<int:page>', views.delete, name="products_delete"),
    path('<int:id>/edit/<int:page>', views.index, name="products_edit"),
    path('<int:page>', views.index, name='products_index_paged'),
    path('', views.index, name='products_index'),
    path('ajax', views.filter, name="products_filter"),
]