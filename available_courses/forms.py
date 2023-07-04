from django import forms
from .models import TeachRequest

class JoinAsLect(forms.ModelForm):
    class Meta:
        model = TeachRequest
        fields = "__all__"