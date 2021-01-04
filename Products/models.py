from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings

#for call user from call "settings.AUTH_USER_MODEL"
import Brand ####
from Accounts.models import Shop


class Product():
#    id =models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brand', verbose_name=_('Brand'), on_delete=models.CASCADE)
                            #related_name='Brand', related_query_name='Brand')
    slug = models.SlugField(_('slug'))
    name = models.CharField(_('product name'))
    image = models.ImageField(_('image'), upload_to='orders/product/images', blank=True, null=True)
    detail = models.CharField(_('product detail'))
    category = models.ForeignKey('Category', verbose_name=_('Category'), on_delete=models.CASCADE)
                            #related_name='Category', related_query_name='Category')
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def __str__(self):
        return self.name


#class ProductMeta(models.Model):
#    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
#                                related_name='meta_field', related_query_name='meta_field')
#    label = models.CharField(_('Label'), max_length=100)
#    value = models.CharField(_('Value'), max_length=100)
#
#    class Meta:
#        verbose_name = _('Product Meta Data')
#        verbose_name_plural = _('Product Meta Detail')
#
#    def __str__(self):
#        return str(self.product) + f'({self.label})'
#


class Category():
#    id =models.AutoField(primary_key=True)
    name = models.CharField(_('product name'))
    slug = models.SlugField(_('slug'))
    detais = models.CharField(_('cateqory detail'))
    image = models.ImageField(_('image'), upload_to='Products/category/images')
#    parent = models.ForeignKey('Parent', verbose_name=_('Parent'), on_delete=models.CASCADE)
                               #related_name='children', related_query_name='children')
#    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True)
#    parent = models.ForeignKey(
#        "self", 
#        verbose_name=_("parent"),
#        related_name='child' ,
#        on_delete=models.SET_NULL,
#        null=True,blank=True
#        ) 
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
 
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')
        
    def __str__(self):
        return self.name



class ShopProduct():
#    id =models.AutoField(primary_key=True)
    shop = models.ForeignKey('Shop', verbose_name=_('Shop'), on_delete=models.CASCADE)
                             #related_name='product_shop', related_query_name='product_shop')
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
                             #related_name='Product', related_query_name='Product')
    price = models.IntegerField(_('product price'))
    quantity = models.IntegerField(_('number of product'))
#    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
#    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    

    class Meta:
        verbose_name = _('shop stor')
        verbose_name_plural = _('shop stor')
        
    def __str__(self):
        return str(self.user)
#        return "shop:"+str(self.shop)+",product"+str(self.product)

class Brand():
#    id =models.AutoField(primary_key=True)
    name = models.ImageField(_('Brand name'))
    details = models.CharField(_('Brand details'))
    image = models.ImageField(_('image'), upload_to='Products/brand/images')
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)
#    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
        
    def __str__(self):
        return self.name


class Images():
#    id =models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
                               #related_name='Product', related_query_name='Product')    
    image = models.ImageField(_('image'), upload_to='Products/images/images')

#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        
    def __str__(self):
        return str(self.product)

#    def __str__(self):
#        return self.name

class off():
#    id =models.AutoField(primary_key=True)
    name = models.CharField(_('off name'), max_length=150)
    number = models.IntegerField(_('number of price off'))
    product = models.ManyToManyField(Product, verbose_name=_('Product'),
                                     #related_name='product', related_query_name='product')    
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('off')
        verbose_name_plural = _('offes')
        
    def __str__(self):
        return self.name


class Comments(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=_('Product'),
                                #related_name='Product', related_query_name='Product')
#    product = models.ForeignKey("Product", verbose_name=_(
#        "Product"),related_name="product_comment", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'),
                             #related_name='User', related_query_name='User')
    text = models.TextField(_('Text'))
#    ONE = 1
#    TWO = 2
#    TREE = 3
#    FOUR = 4
#    FIVE = 5
    RATE = [
        (ONE, 1),
        (TWO, 2),
        (TREE, 3),
        (FOUR, 4),
        (FIVE, 5),
    ]
    rate = models.IntegerField(
        max_length=1,
        choices=RATE,
#        default=ONE,
    )
#    rate = models.IntegerField(_("Rate"))  #how to limited?

#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Comments')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'),
                             #related_name='like', related_query_name='like')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Products liked'),
                                 #related_name='likes', related_query_name='likes')
    like = models.BooleanField(_('like'),default=False)
#    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Like')

    def __str__(self):
        return str(self.user)