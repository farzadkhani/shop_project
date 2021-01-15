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

class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        related_name='basket', 
        related_query_name='basket'
        )
    slug = models.SlugField(_('slug'), unique=True)
    name = models.CharField(_('name'), max_length=500)
    discription = models.CharField(_('discription'), max_length=2000)
    image = models.ImageField(_('image'), upload_to='accounts/shop/images', blank=True)
    products = models.ForeignKey(
        'Products.Product', 
        verbose_name=_('Products'), 
        on_delete=models.CASCADE,
        related_name='basket', 
        related_query_name='basket'
        )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return self.name


class Orders(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('Orders'), 
        on_delete=models.CASCADE,
        related_name='orders', 
        related_query_name='orders'
        )
    slug = models.SlugField(_('slug'), unique=True)
    name = models.CharField(_('name'), max_length=500)
    discription = models.CharField(_('discription'), max_length=2000)
    image = models.ImageField(_('image'), upload_to='accounts/shop/images', blank=True)
    products = models.ForeignKey(
        'Products.Product', 
        verbose_name=_('Products'), 
        on_delete=models.CASCADE,
        related_name='orders', 
        related_query_name='orders'
        )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)


    class Meta:
        verbose_name = _('Orders')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.name


class Peyment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'),
        related_name='payment', 
        related_query_name='payment'
        )
    order = models.ForeignKey(
        'Orders', 
        on_delete=models.CASCADE, 
        verbose_name=_('Order'),
        related_name='payment', 
        related_query_name='payment'
        )
    total_price = models.IntegerField(_('Total price'))
    pey_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return str(self.user)


