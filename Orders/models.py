from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings
from Products.models import ShopProduct
from django.shortcuts import reverse
#for call user from call "settings.AUTH_USER_MODEL"
#import Brand ####

class Basket(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        related_name='Basket', 
        related_query_name='Basket'
        )
    #slug = models.SlugField(_('slug'), unique=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    ordered = models.BooleanField(_("Ordered"), default=False)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return str(self.user)
    
    @property
    def basket_items(self):
        basket_items = BasketItems.objects.filter(basket=self)
        return basket_items

    @property
    def basket_price(self):
        basket_items = self.BasketItems.all()
        total_price = 0
        for i in basket_items:
            total_price += (i.quantity * i.shopproduct.price)
        return total_price


class BasketItems(models.Model):
    basket = models.ForeignKey(
        'Basket', 
        verbose_name=_("Basket"), 
        on_delete=models.CASCADE,
        related_name='BasketItems', 
        related_query_name='BasketItems'
        )
    quantity = models.IntegerField(default=1)
    shopproduct = models.ForeignKey(
        ShopProduct, 
        verbose_name=_("ShopProduct"), 
        on_delete=models.CASCADE,
        related_name='BasketItems', 
        related_query_name='BasketItems'
        )
    @property
    def total_price(self):
        quantity = self.quantity 
        price = self.shopproduct.price
        total = quantity * price
        return total

    ordered = models.BooleanField(_("Ordered"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return str(self.shopproduct)
        #return f'{self.shopproduct.quantity} of {self.shopproduct.title}'


class Orders(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        related_name='Orders', 
        related_query_name='Orders'
        )
    basket = models.OneToOneField(
        'Basket', 
        verbose_name=_('Orders'), 
        on_delete=models.CASCADE,
        related_name='Basket', 
        related_query_name='Basket'
        )
    #slug = models.SlugField(_('slug'), unique=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)



    class Meta:
        verbose_name = _('Orders')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.user)


class Peyment(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'),
        related_name='payment', 
        related_query_name='payment'
        )
    orders = models.OneToOneField(
        'Orders', 
        on_delete=models.CASCADE, 
        verbose_name=_('Orders'),
        related_name='Peyment', 
        related_query_name='Peyment'
        )
    pey_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return str(self.user)


