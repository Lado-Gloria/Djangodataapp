from django import forms
from .models import Shipment


class ShipmentUploadForm(forms.ModelForm):
    class Meta:
        model =Shipment
        fields="__all__"
