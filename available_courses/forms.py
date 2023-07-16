from django import forms
from .models import TeachRequest, MsgRequest

class JoinAsLect(forms.ModelForm):
    class Meta:
        model = TeachRequest
        fields = "__all__"

class SendMsg(forms.ModelForm):
    class Meta:
        model = MsgRequest
        fields = "__all__"