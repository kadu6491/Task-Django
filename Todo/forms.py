from django import forms
from django.forms import ModelForm

from .models import *


class PostTask(forms.ModelForm):

    class Meta(object):
        model = Task
        fields = '__all__'
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
