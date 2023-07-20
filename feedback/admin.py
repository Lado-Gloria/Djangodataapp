from django.contrib import admin
from .models import Feedback

# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'location', 'messages','get_date_created', 'get_date_updated']

    def get_date_created(self, obj):
        return obj.date_created

    def get_date_updated(self, obj):
        return obj.date_updated

    list_display += ['get_date_created', 'get_date_updated']

    get_date_created.short_description = 'Date Created'
    get_date_updated.short_description = 'Date Updated'

admin.site.register(Feedback, FeedbackAdmin)
