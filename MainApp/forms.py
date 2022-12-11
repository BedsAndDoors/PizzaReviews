from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        label = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}