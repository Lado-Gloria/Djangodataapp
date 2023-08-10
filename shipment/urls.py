from django.urls import path
from . import views

app_name = 'shipment'

urlpatterns = [
    path('shipments/upload/', views.upload_shipment, name='upload_shipment'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('shipments/<int:id>/', views.shipment_detail, name='shipment_detail_view'),
    path('shipments/<int:id>/edit/', views.edit_shipment_view, name='edit_shipment'),
]