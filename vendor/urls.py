from django.urls import path
from . import views

app_name = 'vendor'

urlpatterns = [
    path('vendors/upload/', views.upload_vendor, name='upload_vendor'),
    path('vendors/', views.vendor_list, name='vendor_list'),  # This URL pattern is for listing vendors
    path('vendors/<int:id>/', views.vendor_detail, name='vendor_detail_view'),
    path('vendors/<int:id>/edit/', views.edit_vendor_view, name='edit_vendor'),
]

