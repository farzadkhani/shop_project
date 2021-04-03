from django.contrib.auth.forms import UserCreationForm
from .models import User, Address, Shop
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email', 'mobile', 'first_name', 'last_name', 'image')
        labels = {
            'email':_('ایمیل'), 
            'mobile':_('شماره مبایل'),
            'first_name':_('نام'),
            'last_name':_('نام خانوادگی'),
            'image':_('تصویر شما'),
            'password':_('رمز عبور'), 
            'password2':_('تکرار رمز عبور'),
            }
        widget = {
            'email':forms.EmailInput(),#attrs={'class':'form-control'
            'mobile':forms.IntegerField(),#attrs={'class':'form-control'}
            'first_name':forms.TextInput(),#attrs={'class':'form-control'}
            'last_name':forms.TextInput(),#attrs={'class':'form-control'}
            'image':forms.ImageField(),#attrs={'class':'form-control'}
            'password':forms.PasswordInput(),#attrs={'class':'form-control'}
            'password2':forms.PasswordInput(),#attrs={'class':'form-control'}
        }
        help_text = {'email':_('a valid email for reser your password'), }


class MyProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')   #get user and remove it from 'kwargs'
        super(MyProfileForm, self).__init__(*args, **kwargs)
        #for disable the edit some fields we can do this
        if not user.is_superuser:
            self.fields['mobile'].disabled = True
            self.fields['email'].disabled = True
        #make help_text.required to call in template, for example "{{ form.first_name.help_text }}"
        self.fields['first_name'].help_text = 'لطفا نام خود را وارد کنید'
        self.fields['last_name'].help_text = 'لطفا نام خانوادکی خودرا وارد کنید'
        self.fields['mobile'].help_text = 'شماره موبایل بدون صفر اول وارد شود'
        self.fields['email'].help_text = 'ایمل باید به شکل این مثال باشد YourName@gmail.com'
        self.fields['image'].help_text = 'توجه: فرار دادن عکس الزامی نیست'
   
    class Meta:
        model = User
        fields = [
            'email', 'mobile', 'first_name', 'last_name', 'image'
            ]


class MyAddressProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(MyAddressProfileForm, self).__init__(*args, **kwargs)

        self.fields['city'].help_text = 'نام شهر خود را وارد کنید'
        # self.fields['street'].help_text = 'خیابان محل سکونت'
        # self.fields['number'].help_text = 'شماره پلاک'
        # self.fields['zip_code'].help_text = 'کد پستی ۱۰ رقمی'

    class Meta:
        model = Address
        fields = [
            'city', 'street', 'number', 'zip_code', 'name',
            ]

# class NewAddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = [
#             'city', 'street', 'number',
#         ]


class MyShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name', 'slug', 'facebook', 
            'instagram', 'telegram', 'whatsapp', 
            'discription', 'image'
        ]