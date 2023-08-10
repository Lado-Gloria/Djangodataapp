from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('orders/upload/', views.upload_orders, name='upload_orders'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/<int:id>/', views.orders_detail, name='orders_detail_view'),
    path('orders/<int:id>/edit/', views.edit_orders_view, name='edit_orders'),
]