from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'product' ) #, 'image','slug', 'created', 'updated'
    search_fields = ('user', 'name', 'product' ) #, 'image','slug', 'created', 'updated'
    list_filter = ('user', 'name', 'product')

#    class Meta:
#        ordering = ('status', 'closed')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'products') #, 'created', 'updated'
    search_fields = ('shop', 'product') #, 'created', 'updated'
    list_filter = ('shop', 'product') #, 'created', 'updated'




@admin.register(Peyment)
class PeymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'total_price', 'pay_date') #, 'created', 'updated'
    search_fields = ('user', 'order', 'total_price', 'pay_date') #, 'created', 'updated'
    list_filter = ('user')   #, 'created', 'updated'

#    class Meta:
#        ordering = ['-quantity', 'price']