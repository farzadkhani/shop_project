from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from django.urls import reverse
from django.apps import apps
from django.db.models import Min, Max


# for call user from call "settings.AUTH_USER_MODEL"


class Product(models.Model):  # make product data
    brand = models.ForeignKey(
        'Brand',
        verbose_name=_('Brand'),
        on_delete=models.CASCADE,
        related_name='Product',
        # similar as 'product_set' in  Branditem.product_set.all() or similar as Branditem.Product.all()
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

    @property
    def find_all_size_and_color(self):
        refrence = ShopProduct.objects.filter(product=self).order_by('size')
        final_list = []
        size_list = []
        for i in refrence:
            if not i.size.name in size_list:
                size_list.append(i.size.name)
                refrence2 = ShopProduct.objects.filter(product=self, size__name=i.size.name).order_by('price')
                check_list = []
                refrence3 = []
                for b in refrence2:
                    if not b.color in check_list:
                        check_list.append(b.color)
                        refrence3.append(b)
                # print('refrence2', refrence3)
                temp = [refrence3]
                # print('temp', temp)
                temprory = [i.size.name, temp]
                final_list.append(temprory)
        # print('final', final_list[1][1][0][0].color)
        return final_list

    @property
    def min_price(self):
        # ShopProduct = apps.get_model(app_label='Products', model_name='ShopProduct' )
        shop_product = self.ShopProduct.order_by('price')
        return shop_product

    @property
    def first_min_price(self):
        # ShopProduct = apps.get_model(app_label='Products', model_name='ShopProduct' )
        shop_product = self.ShopProduct.order_by('price')
        # print('shop_product', shop_product)
        # print('first min price', type(shop_product), shop_product)
        if self.find_all_size_and_color:
            return shop_product[0].price


    def first_min_price_(self):
        # ShopProduct = apps.get_model(app_label='Products', model_name='ShopProduct' )
        shop_product = self.ShopProduct.order_by('price')
        # print('shop_product', shop_product)
        # print('first min price', type(shop_product), shop_product)
        if self.find_all_size_and_color:
            return shop_product[0].price


    def __str__(self):
        return self.name

    def image_tag(self):
        image = self.image
        if image:
            return mark_safe('<img src="{}" height="50"/>'.format(image.url))
        else:
            return ""


class ProductMeta(models.Model):  # product size and coloar
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


class Category(models.Model):  # make cagories
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

    @property
    def get_all_sub_childrens_(self):
        first = self.children.all()
        final_list = []
        temprory_list = []
        for i in first:
            final_list.append(i)
            temprory_list.append(i)
        while len(temprory_list) > 0:
            for i in temprory_list:
                object_ = Category.objects.filter(parent__id=i.id)
                temprory_list.remove(i)
                for j in object_:
                    temprory_list.append(j)
                for j in object_:
                    final_list.append(j)
        # print('final_list', final_list)
        return final_list

    def get_all_childrens(self):
        # return all children 'full objects' of the curent category
        children = self.children.all()
        return children

    @property
    def get_parent(self):
        parent = self.parent
        return parent

    @property
    def category_road(self):
        # show the all parents of curent category
        check = Category.objects.filter(name=self.name)
        parents = []
        parents.append(check[0])
        while check[0].get_parent:
            parents.insert(0, check[0].get_parent)
            check = Category.objects.filter(name=check[0].get_parent)
        return parents

    # def get_absolute_url(self):
    #    return reverse("search_product", kwargs={"slug": self.slug})


class ShopProduct(models.Model):  # for price and quantity relate with product and shop{saler}
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
    size = models.ForeignKey(
        'Size',
        verbose_name=_('Size'),
        on_delete=models.CASCADE,
        related_name='ShopProduct',
        related_query_name='ShopProduct',
    )
    color = models.ForeignKey(
        'Color',
        verbose_name=_('Color'),
        on_delete=models.CASCADE,
        related_name='ShopProduct',
        related_query_name='ShopProduct',
    )
    # parent_self = models.ForeignKey('ShopProduct', on_delete=models.CASCADE, null=True , blank=True)
    price = models.PositiveIntegerField(_('product price'))
    quantity = models.IntegerField(_('number of product'))
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    # shop and product should be uniq to gether
    # unique_toghether
    class Meta:
        verbose_name = _('ShopProduct')
        verbose_name_plural = _('ShopProducts')
        unique_together = ['shop', 'product', 'color', 'size']

    @property
    def min_off(self):
        Off = apps.get_model(app_label='Products', model_name='Off')
        off = self.Off
        # print('off', off)
        return off

    def __str__(self):
        return "فروشگاه:" + str(self.shop) + '---' + ",محصول:" + str(self.product)

    def image_tag(self):
        image = self.product.image
        if image:
            return mark_safe('<img src="{}" height="50"/>'.format(image.url))
        else:
            return ""

    @property
    def find_all_same_size_and_color(self):
        self_size = self.size.name
        self_color = self.color.name
        self_product = self.product.id
        all_shopProducts = ShopProduct.objects.filter(product__id=self_product, size__name=self_size,
                                                      color__name=self_color).order_by('price')
        return all_shopProducts


class Off(models.Model):  # add off on product
    shop_product = models.OneToOneField(
        'ShopProduct',
        verbose_name=_('Shop_product'),
        on_delete=models.PROTECT,
        related_name='Off',
        related_query_name='Off',
        null=True,
        blank=True
    )

    name = models.CharField(_('off name'), max_length=150)
    price = models.IntegerField(_('number of price off'))
    # product = models.ForeignKey(
    #    'Product',
    #    on_delete=models.CASCADE,
    #    verbose_name=_('Product'),
    #    related_name='Off', 
    #    related_query_name='Off'
    #    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)

    class Meta:
        verbose_name = _('Off')
        verbose_name_plural = _('Offes')

    def __str__(self):
        return self.name


class Brand(models.Model):  # make brand of product
    name = models.CharField(_('Brand name'), max_length=1000)
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


class Image(models.Model):  # for more images
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


class Color(models.Model):
    name = models.CharField(_('color name'), max_length=500)
    code = models.CharField(_("color code"), max_length=50)

    def __str__(self):
        return self.name

    def color_tag(self):
        code = self.code
        if self.code:
            return mark_safe('<p style="background-color:{}">Color</p>'.format(self.code))
        else:
            pass


class Size(models.Model):
    name = models.CharField(_('product name'), max_length=500)
    code = models.CharField(_('size code'), max_length=50)

    # category = models.ForeignKey(
    #     'Category', 
    #     verbose_name=_('Category'), 
    #     on_delete=models.CASCADE,
    #     related_name='Size', 
    #     related_query_name='Size'
    #     )

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
        # max_length=1,
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
    like = models.BooleanField(_('like'), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _('Like')

    def __str__(self):
        return str(self.user)
