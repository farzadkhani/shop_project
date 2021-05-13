from django.contrib import admin
from django.contrib.admin.sites import site
from django.utils.translation import ugettext_lazy as _
from . import models

# Register your models here.

class ProductMetaTabularInline(admin.TabularInline):
    model = models.ProductMeta
    extra = 1
    # exclude = ('text_name', )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMetaTabularInline]
    fieldsets = (
        (None, {
            "fields": ('brand', 'slug'),
        }),
        ('first', {
            "fields": ('name',),
        }),
        ('second', {
            "fields": ('detail', 'category', 'publish_time'),
        }),
        ('third', {
            "fields": ('is_amazing_offer', ),
        }),
    )
    
    list_display = ('id', 'name', 'category', 'brand', 'slug', 'combine_name_and_brand',  'is_amazing_offer')    #, 'created', 'updated', imgage_tag
    search_fields = ('id', 'name', 'slug', 'brand', 'category', 'is_amazing_offer')
    list_filter = ('created_at', 'updated_at', 'publish_time', 'is_amazing_offer')
    list_display_links = ('name', 'brand', 'is_amazing_offer')
    
    def combine_name_and_brand(self, obj):
        return "{} برند {}".format(obj.name, obj.brand)


@admin.register(models.ProductMeta)
class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ('product',)    #, 'created', 'updated'
    search_fields = ('product',)
    list_filter = ('product',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug' ,'parent_id', 'parent', 'detail')    # 'parent', 'create', 'update'
    search_fields = ('name', 'slug')    #'parent'
    list_filter = ('created_at', 'updated_at', 'publish_time')


# class InLineShopProduct(admin.TabularInline):
#     model = models.ShopProduct
#     extra = 1
#     #max_num = 3    #max number of extra

@admin.register(models.ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    # inlines = [InLineShopProduct]
    list_display = ('id', 'product', 'shop', 'price', 'size', 'color') # 'quantity', 'create', 'update', 'image_tag'
    search_fields = ('product', 'price', 'shop', 'quantity')
    list_filter = ('created_at', 'updated_at', 'publish_time')
    list_display_links = ('shop', )# 'parent_self', 

    class Meta:
        ordering = ['-quantity', 'price']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'image', 'is_special', ) #,'create', 'update'
    search_fields = ('name', 'detail', 'is_special')
    list_filter = ('created_at', 'updated_at', 'publish_time', 'is_special')


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image') #, 'created', 'updated'
    search_fields = ('product',)
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'color_tag') #, 'created', 'updated'
    search_fields = ('name', 'code')
    list_filter = ('name', 'code')


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code') #, 'created', 'updated'
    search_fields = ('name', 'code')
    list_filter = ('name', 'code')


@admin.register(models.Off)
class OffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'shop_product')  #, 'created', 'updated'
    search_fields = ('name', 'price', 'product') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'text', 'is_active')  #, 'created', 'updated'
    search_fields = ('product', 'user', 'text', 'is_active') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at')


@admin.register(models.CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'like')  #, 'created', 'updated'
    search_fields = ('user', 'comment', 'like') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at')
#     #fields = '__all__'
#     # fieldsets = (
#     #     (None, {
#     #         "fields": (
                
#     #         ),
#     #     }),
#     # )
#     # inlines = []
#     #add_form = 


@admin.register(models.CommentDisLike)
class CommentDisLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'dislike')  #, 'created', 'updated'
    search_fields = ('user', 'comment', 'dislike') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at')


@admin.register(models.WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user','product')
    search_fields = ('user','product')
    list_filter = ('user','product')