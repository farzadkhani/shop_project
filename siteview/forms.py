from django import forms
from django.utils.translation import ugettext_lazy as _
from Products.models import Product
from django.forms import Textarea, DateTimeField
#from django.forms import MultiWidget
from django.contrib.admin import widgets                                       

class ProductForm(forms.Form):
    name = forms.CharField(required=False)

class ProductAttrsForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("brand", "category")

    
