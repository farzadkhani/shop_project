from django.urls import path
from .views import (
    ProductListCategory, ProductListSeller, 
    ProductDetail, SearchInProducts, 
    SellerShopProduct, remove_prodcut_from_store, 
    SellerEditShopProduct
    )
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('category/<slug:slug>/', ProductListCategory.as_view(), name='search_product'),
    path('search/', SearchInProducts.as_view(), name='search'),
    path('seller/<slug:slug>/', ProductListSeller.as_view(), name='search_product_seller'),
    path('create_new_product/', SellerShopProduct.as_view(), name='create_new_product'),
    path('edit_product/<str:product>/<str:size>/<str:color>/', SellerEditShopProduct.as_view(), name='edit_product'),
    path('remove_product_from_store/<int:id>/', remove_prodcut_from_store, name='remove_prodcut_from_store'),
    path('product/<slug:slug>/<int:id>/', ProductDetail.as_view(), name='detail_product'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='detail_product_not_seller'),

    #Basket Urls
    #path('increase_from_basket/<int:id>/', increase_from_basket, name='increase_from_basket'),
]

