from django.urls import path
from .views import (
    ProductListCategory, ProductListSeller, 
    ProductDetail, SearchInProducts, 
    SellerShopProduct, remove_prodcut_from_store, 
    SellerEditShopProduct,
    add_to_wish_list,
    WishListView,
    CommentLikeView,
    CommentDisLikeView
    )
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('category/<slug:slug>/', ProductListCategory.as_view(), name='search_product'),
    path('search/', SearchInProducts.as_view(), name='search'),
    path('seller/<slug:slug>/', ProductListSeller.as_view(), name='search_product_seller'),
    path('create_new_product/<str:product>/', SellerShopProduct.as_view(), name='create_new_product'),
    path('edit_product/<int:id>/<str:size>/<str:color>/', SellerEditShopProduct.as_view(), name='edit_product'),
    path('remove_product_from_store/<int:id>/', remove_prodcut_from_store, name='remove_prodcut_from_store'),
    path('product/<slug:slug>/<int:id>/', ProductDetail.as_view(), name='detail_product'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='detail_product_not_seller'),
    path('add_to_wish_list/<int:id>/<slug:slug>/', add_to_wish_list, name='add_to_wish_list'),
    path('wish_list/', WishListView.as_view(), name='wish_list'),
    path('comment_like/<int:pk>/<slug:slug>/<int:id>/', CommentLikeView.as_view(), name='comment_like'),
    path('comment_dislike/<int:pk>/<slug:slug>/<int:id>/', CommentDisLikeView.as_view(), name='comment_dislike'),
    

    #Basket Urls
    #path('increase_from_basket/<int:id>/', increase_from_basket, name='increase_from_basket'),
]

