from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

#for call user from call "settings.AUTH_USER_MODEL"



class Product(models.Model):    #make product data
    brand = models.ForeignKey(
        'Brand', 
        verbose_name=_('Brand'), 
        on_delete=models.CASCADE,
        related_name='Product', 
        related_query_name='Product'
        )
    slug = models.SlugField(_('slug'))
    name = models.CharField(_('product name'), max_length=500)
    image = models.ImageField(_('image'), upload_to='orders/product/images', blank=True, null=True)
    detail = models.CharField(_('product detail'), max_length=2000, blank=True, null=True)
    category = models.ForeignKey(
        'Category', 
        verbose_name=_('Category'), 
        on_delete=models.CASCADE,
        related_name='Product', 
        related_query_name='Product'
        )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def __str__(self):
        return self.name


class ProductMeta(models.Model):    #product size and coloar
    product = models.ForeignKey(
        'Product', 
        on_delete=models.CASCADE, 
        verbose_name=_('Product'),
        related_name='ProductMeta', 
        related_query_name='ProductMeta'
        )
    

    class Meta:
        verbose_name = _('ProductMeta')
        verbose_name_plural = _('ProductMetas')

    def __str__(self):
        return str(self.product)


class Category(models.Model):   #make cagories
    name = models.CharField(_('product name'), max_length=500)
    slug = models.SlugField(_('slug'))
    detail = models.CharField(_('cateqory detail'), max_length=2000, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='Products/category/images', blank=True, null=True)
    parent = models.ForeignKey(
        "self", 
        verbose_name=_("Parent"),
        related_name=_("children"),
        related_query_name=_("children"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        ) 
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        
    def __str__(self):
        return self.name
    
    def get_all_childrens(self):
        #return all children 'full objects' of the curent category
        children = self.children.all()
        return children

    def get_parent(self):
        parent = self.parent
        return parent


    def get_all_parents(self):
        #show the all parents of curent category
        parents = []
        if self.parent is not None:
            parent = self.parent
            parents.append(parent)
        return parents
    
    #def get_absolute_url(self):
    #    return reverse("search_product", kwargs={"slug": self.slug})


class ShopProduct(models.Model):    #for price and quantity relate with product and shop{saler}
    shop = models.ForeignKey(
        'Accounts.Shop', 
        verbose_name=_('Shop'), 
        on_delete=models.CASCADE,
        related_name='ShopProduct', 
        related_query_name='ShopProduct'
        )
    product = models.ForeignKey(
        'Product', 
        verbose_name=_('Product'), 
        on_delete=models.CASCADE,
        related_name='ShopProduct', 
        related_query_name='ShopProduct'
        )
    price = models.IntegerField(_('product price'))
    quantity = models.IntegerField(_('number of product'))
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)
    
    #shop and product should be uniq to gether
    #unique_toghether
    class Meta:
        verbose_name = _('ShopProduct')
        verbose_name_plural = _('ShopProducts')
        unique_together = ['shop', 'product']
        
    def __str__(self):
        return "shop:"+str(self.shop)+",product"+str(self.product)


class Brand(models.Model):  #make brand of product
    name = models.CharField(_('Brand name'), max_length= 1000)
    details = models.CharField(_('Brand details'), max_length=5000, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='Products/brand/images', blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)
    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
        
    def __str__(self):
        return self.name


class Image(models.Model):  #for more images
    product = models.ForeignKey(
        'Product', 
        verbose_name=_('Product'), 
        on_delete=models.CASCADE,
        related_name='Images', 
        related_query_name='Image'
        )    
    image = models.ImageField(_('Image'), upload_to='Products/images/images', blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        
    def __str__(self):
        return str(self.product)


class Off(models.Model):    #add off on product
    name = models.CharField(_('off name'), max_length=150)
    price = models.IntegerField(_('number of price off'))
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='Off', 
        related_query_name='Off'
        )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Off')
        verbose_name_plural = _('Offes')
        
    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        'Product', 
        on_delete=models.CASCADE, 
        verbose_name=_('Product'),
        related_name='Comment', 
        related_query_name='Comments'
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'),
        related_name='Comment', 
        related_query_name='Comments'
        )
    text = models.TextField(_('Text'))
    rate = models.IntegerField(
        #max_length=1,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'),
        related_name='Like', 
        related_query_name='Likes'
        )
    product = models.ForeignKey(
        'Product', 
        on_delete=models.CASCADE, 
        verbose_name=_('Product'),
        related_name='Like', 
        related_query_name='Likes'
        )
    like = models.BooleanField(_('like'),default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _('Like')

    def __str__(self):
        return str(self.user)