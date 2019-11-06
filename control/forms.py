from django import forms
from .models import StoreUrl


class GivenUrl(forms.ModelForm):
    class Meta:
        model = StoreUrl
        fields = ("given_url",)
