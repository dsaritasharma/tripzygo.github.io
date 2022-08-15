from django import forms
from .models import package


class packageform(forms.ModelForm):
    class Meta:
        model=package
        fields="__all__"
       