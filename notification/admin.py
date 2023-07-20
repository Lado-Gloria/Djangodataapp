from django.contrib import admin
# Register your models here.
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name","contact","message")
admin.site.register(Notification,NotificationAdmin)