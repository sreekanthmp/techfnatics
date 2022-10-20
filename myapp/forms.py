from django import forms
from .models import Contact,Image,Products, Socialmedia, Text

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        

class Productform(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"
        

class Imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields="__all__"
        

class Textform(forms.ModelForm):
    class Meta:
        model=Text
        fields="__all__"
        

class Mediaform(forms.ModelForm):
    class Meta:
        model=Socialmedia
        fields="__all__"