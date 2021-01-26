from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings
from Products.models import ShopProduct
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
    

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return str(self.user)


class BasketItems(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        related_name='BasketItems', 
        related_query_name='BasketItems'
        )
    basket = models.ForeignKey(
        'Basket', 
        verbose_name=_("Basket"), 
        on_delete=models.CASCADE,
        related_name='BasketItems', 
        related_query_name='BasketItems'
        )
    shopproduct = models.ForeignKey(
        ShopProduct, 
        verbose_name=_("ShopProduct"), 
        on_delete=models.CASCADE,
        related_name='BasketItems', 
        related_query_name='BasketItems'
        )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return str(self.user)

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


