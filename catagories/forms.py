from django import forms
from . import models

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = models.Catagory
        fields = '__all__'
        