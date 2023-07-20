from django.contrib import admin
from orders.models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'orderName', 'orderNumber', 'orderTotal','get_date_created', 'get_date_updated']
    def get_date_created(self, obj):
        return obj.date_created
    def get_date_updated(self, obj):
        return obj.date_updated
    list_display += ['get_date_created', 'get_date_updated']
    get_date_created.short_description = 'Date Created'
    get_date_updated.short_description = 'Date Updated'
admin.site.register(Order, OrderAdmin)