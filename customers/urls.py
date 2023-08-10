from django.urls import path
from . import views

urlpatterns = [
    path("customers/upload/", views.upload_customer, name="customer_upload_view"),
    path("customers/<int:id>/", views.customer_detail, name="customer_detail_view"),
    path("customers/list/", views.customer_list, name="customer_list_view"),
    path("customers/edit/<int:id>/", views.edit_customer_view, name="customer_edit_view"),
]

