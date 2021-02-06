from django.contrib import admin
from django.contrib.admin.sites import site
from django.utils.translation import ugettext_lazy as _
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'slug')    #, 'created', 'updated'
    search_fields = ('name', 'slug', 'brand', 'category')
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.ProductMeta)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product',)    #, 'created', 'updated'
    search_fields = ('product',)
    list_filter = ('product',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug' ,'parent_id', 'parent', 'detail')    # 'parent', 'create', 'update'
    search_fields = ('name', 'slug')    #'parent'
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ('shop', 'product', 'price', 'quantity') #'create', 'update'
    search_fields = ('product', 'price', 'shop', 'quantity')
    list_filter = ('created_at', 'updated_at', 'publish_time')

    class Meta:
        ordering = ['-quantity', 'price']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'image' ) #,'create', 'update'
    search_fields = ('name', 'detail')
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image') #, 'created', 'updated'
    search_fields = ('product',)
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.Off)
class OffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product')  #, 'created', 'updated'
    search_fields = ('name', 'price', 'product') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at', 'publish_time')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'text', 'rate')  #, 'created', 'updated'
    search_fields = ('product', 'user', 'text', 'rate') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at')



@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'like')  #, 'created', 'updated'
    search_fields = ('user', 'product', 'like') #, 'created', 'updated'
    list_filter = ('created_at', 'updated_at')
