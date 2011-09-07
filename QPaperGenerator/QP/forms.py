#!/usr/bin/python
from django.forms import ModelForm
from django import forms
from QPaperGenerator.QP.models import *
from django.forms.extras.widgets import *



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


    
    
