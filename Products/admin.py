from django.contrib import admin
from django.contrib.admin.sites import site
from django.utils.translation import ugettext_lazy as _
#
#
## Register your models here.
#
#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('name', 'category', 'brand', 'slug')    #, 'created', 'updated'
#    search_fields = ('name', 'slug', 'brand', 'category')
#    list_filter = ('brand', 'category', 'created', 'updated')
#
#
#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('name', 'slug', 'image', 'detail')    # 'parent', 'create', 'update'
#    search_fields = ('name', 'slug')    #'parent'
##    list_filter = ('create', 'update')
#
#
#@admin.register(ImageGallery)
#class ShopProductAdmin(admin.ModelAdmin):
#    list_display = ('shop', 'product', 'price', 'quantity') #'create', 'update'
#    search_fields = ('product', 'price', 'shop', 'quantity')
##    list_filter = ('created', 'updated')
#
##    class Meta:
#        ordering = ['-quantity', 'price']

#@admin.register(Brand)
#class BrandAdmin(admin.ModelAdmin):
#    list_display = ('name', 'detail', 'image' ) #,'create', 'update'
#    search_fields = ('name', 'detail')
##    list_filter = ('create', 'update')
#
#
#@admin.register(ImageGallery)
#class ImageGalleryAdmin(admin.ModelAdmin):
#    list_display = ('product', 'image') #, 'created', 'updated'
#    search_fields = ('product',)
##    list_filter = ('created', 'updated')
#
#
#@admin.register(ProductMeta)
#class OffAdmin(admin.ModelAdmin):
#    list_display = ('name', 'number', 'product')    #, 'created', 'updated'
#    search_fields = ('name', 'number')
##    list_filter = ('created', 'updated')
#
#
#@admin.register(ProductMeta)
#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('product', 'user', 'text', 'rate')  #, 'created', 'updated'
#    search_fields = ('product', 'user', 'text', 'rate') #, 'created', 'updated'
##    list_filter = ('created', 'updated')
#
#
#@admin.register(Like)
#class LikeAdmin(admin.ModelAdmin):
#    list_display = ('user', 'product', 'like')  #, 'created', 'updated'
#    search_fields = ('user', 'product', 'like') #, 'created', 'updated'
##    list_filter = ('created', 'updated')