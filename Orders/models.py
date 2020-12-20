from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings
#for call user from call "settings.AUTH_USER_MODEL"
#import Brand ####
from Accounts.models import Shop

class Product():
    #id =models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brand', verbose_name=_('Brand'), on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'))
    name = models.CharField(_('product name'))
    image = models.ImageField(_('image'), upload_to='orders/product/images')
    detail = models.CharField(_('product detail'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def __str__(self):
        return self.brand


class Category():
    #id =models.AutoField(primary_key=True)
    name = models.CharField(_('product name'))
    slug = models.SlugField(_('slug'))
    detais = models.CharField(_('cateqory detail'))
    image = models.ImageField(_('image'), upload_to='orders/category/images')
    #parent = models.ForeignKey(Parent, verbose_name=_('Parent'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')
        
    def __str__(self):
        return self.name



class ShopProduct():
    #id =models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, verbose_name=_('Shop'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
    name = models.ImageField(_('product price'))
    quantity = models.ImageField(_('number of product'))
    

    class Meta:
        verbose_name = _('shop stor')
        verbose_name_plural = _('shop stor')
        
    def __str__(self):
        return self.name


class Brand():
    #id =models.AutoField(primary_key=True)
    name = models.ImageField(_('Brand name'))
    details = models.CharField(_('Brand details'))
    image = models.ImageField(_('image'), upload_to='orders/brand/images')
    

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
        
    def __str__(self):
        return self.name


class Images():
    #id =models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='orders/images/images')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        
    def __str__(self):
        return self.name


class off():
    #id =models.AutoField(primary_key=True)
    name = models.CharField(_('off name'))
    number = models.IntegerField(_('number of price of'))
    

    class Meta:
        verbose_name = _('off')
        verbose_name_plural = _('offes')
        
    def __str__(self):
        return self.name



