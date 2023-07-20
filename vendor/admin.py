from django.contrib import admin
from vendor.models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'get_date_created', 'get_date_updated']

    def get_date_created(self, obj):
        return obj.date_created

    def get_date_updated(self, obj):
        return obj.date_updated

    get_date_created.admin_order_field = 'date_created'
    get_date_created.short_description = 'Date Created'
    get_date_updated.admin_order_field = 'date_updated'
    get_date_updated.short_description = 'Date Updated'

admin.site.register(Vendor, VendorAdmin)