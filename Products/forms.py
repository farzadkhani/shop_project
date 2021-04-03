from .models import ShopProduct
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets                                       


class SellerShopProductForm(forms.ModelForm):
    # publish_time =  forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    publish_time = forms.DateTimeField(widget=forms.SelectDateWidget())
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['publish_time'].widget = widgets.AdminSplitDateTime()
    class Meta:
        model = ShopProduct
        fields = [
            'product', 'size', 'color', 
            'price', 'quantity', 'publish_time', 
        ]
        # widgets = {
        #     'publish_time': forms.DateTimeInput(
        #          attrs={'class' : 'date_picker'})
        # }
        # widgets = {
        #     'publish_time': widgets.AdminDateWidget()
        # }
    # publish_time = DateTimeField(widget=MinimalSplitDateTimeMultiWidget())