from django.urls import path
from . import views

urlpatterns = [
    path("carts/upload/", views.upload_cart, name="upload_cart"),
    path("carts/<int:id>/", views.cart_detail, name="cart_detail_view"),
    path("carts/list/", views.cart_list, name="cart_list_view"),
    path("carts/edit/<int:id>/", views.edit_cart_view, name="product_edit_view"),
]