from django import forms
from .models import *

class ContentForm(forms.ModelForm):
  class Meta:
    model = Content
    fields = ['content']
    widgets = {
      'content': forms.FileInput(attrs={'id': 'content'}),
    }

class StyleForm(forms.ModelForm):
  class Meta:
    model = Style
    fields = ['style']
    widgets = {
      'style': forms.FileInput(attrs={'id': 'style'}),
    }
