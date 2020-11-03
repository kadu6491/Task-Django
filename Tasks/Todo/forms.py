from django import forms
from django.forms import ModelForm

from .models import *


class PostTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
