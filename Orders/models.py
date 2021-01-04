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
from Products.models import Product
from Accounts.models import Shop


class Basket():
    #id =models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE)
                            #related_name='Basket', related_query_name='Basket')
#    slug = models.SlugField(_('slug'), unique=True)
    name = models.CharField(_('name'))
#    discription = models.CharField(_('discription'))
#    image = models.ImageField(_('image'), upload_to='accounts/shop/images', blank=True)
    products = models.ManyToManyField(Product, verbose_name=_('User'), on_delete=models.CASCADE)
                            #related_name='Orders', related_query_name='Orders')
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return self.name


class Orders():
    #id =models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE)
                            #related_name='Orders', related_query_name='Orders')
#    slug = models.SlugField(_('slug'), unique=True)
    name = models.CharField(_('name'))
#    discription = models.CharField(_('discription'))
#    image = models.ImageField(_('image'), upload_to='accounts/shop/images', blank=True)
    products = models.ManyToManyField(Product, verbose_name=_('User'), on_delete=models.CASCADE)
                            #related_name='Orders', related_query_name='Orders')
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)


    class Meta:
        verbose_name = _('Orders')
        #verbose_name_plural = _('Orders')

    def __str__(self):
        return self.name


class Peyment():
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'),
    #                         related_name='payment', related_query_name='payment')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=_('Order'),
    #                             related_name='payment', related_query_name='payment')
    total_price = models.IntegerField(_('Total price'))
    pay_date = models.DateTimeField(_('Pay date'), auto_now_add=True)
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return str(self.user)


