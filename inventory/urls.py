from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('products/upload/', views.upload_product, name='upload_product'),
    path('products/', views.products_list, name='products_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail_view'),
    path('products/<int:id>/edit/', views.edit_product_view, name='edit_product'),
]