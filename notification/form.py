from django import forms
from .models import Notification


class NotificationUploadForm(forms.ModelForm):
    class Meta:
        model =Notification
        fields="__all__"
