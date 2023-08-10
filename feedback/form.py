from django import forms
from .models import Feedback


class FeedbackUploadForm(forms.ModelForm):
    class Meta:
        model =Feedback
        fields="__all__"
