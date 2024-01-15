from django import forms
from .models import AppModel

class AppForm(forms.ModelForm):
    
    class Meta:
    
        model = AppModel

        fields = [
            "title",
            "description",
        ]