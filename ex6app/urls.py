# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # List all products
    path('create/', views.product_create, name='product_create'),  # Insert new product
    path('update/<int:pk>/', views.product_update, name='product_update'),  # Update product by ID
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),  # Delete product by ID
]
