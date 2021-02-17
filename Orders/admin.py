from django.contrib import admin
from .models import Basket, Orders, Peyment, BasketItems
# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'basket_items','updated_at') #'created', 'updated'
    search_fields = ('user', 'updated_at') #'created', 'updated'
    list_filter = ('user','updated_at')

    class Meta:
        ordering = ('updated_at',)


@admin.register(BasketItems)
class BasketItemsAdmin(admin.ModelAdmin):
    list_display = ('basket', 'quantity', 'shopproduct', 'updated_at') #'created', 'updated'
    search_fields = ('basket', 'shopproduct', 'updated_at') #'created', 'updated'
    list_filter = ('basket', 'shopproduct', 'updated_at')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'basket') #, 'created', 'updated'
    search_fields = ('user', 'basket') #, 'created', 'updated'
    list_filter = ('user', 'basket') #, 'created', 'updated'



@admin.register(Peyment)
class PeymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'orders', 'created_at') #, 'created', 'updated'
    search_fields = ('user', 'orders', 'created_at') #, 'created', 'updated'
    list_filter = ('user',)   #, 'created', 'updated'

#    class Meta:
#        ordering = ['-quantity', 'price']