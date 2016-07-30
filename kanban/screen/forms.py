from django.forms import inlineformset_factory
from django import forms
from .models import *

class TestForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('id','name',)

