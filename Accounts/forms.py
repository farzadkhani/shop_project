from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.utils.translation import gettext_lazy as _

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