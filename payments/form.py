from django import forms
from .models import Payments


class PaymentsUploadForm(forms.ModelForm):
    class Meta:
        model =Payments
        fields="__all__"
