from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('notification/upload/', views.upload_notification, name='upload_notification'),
    path('notification/', views.notification_list, name='notification_list'),
    path('notification/<int:id>/', views.notification_detail, name='notification_detail_view'),
    path('notification/<int:id>/edit/', views.edit_notification_view, name='edit_notification'),
]