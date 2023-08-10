from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('payments/upload/', views.upload_payments, name='upload_payments'),
    path('payments/', views.payments_list, name='payments_list'),
    path('payments/<int:id>/', views.payments_detail, name='payments_detail_view'),
    path('payments/<int:id>/edit/', views.edit_payments_view, name='edit_payments'),
]