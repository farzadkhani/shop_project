from .models import ShopProduct, Comment
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets                                       


class SellerShopProductForm(forms.ModelForm):
    # publish_time =  forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    publish_time = forms.DateTimeField(widget=forms.SelectDateWidget())
    # price = forms.IntegerField(widget=forms.TextInput(attrs={'onclick':'commas(self)'}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['publish_time'].widget = widgets.AdminSplitDateTime()
    class Meta:
        model = ShopProduct
        fields = [
            'size', 'color', 
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]