from django.urls import path
from .views import ProductListCategory, ProductListSeller, ProductDetail
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('search/<slug:slug>/', ProductListCategory.as_view(), name='search_product'),
    path('seller/<slug:slug>/', ProductListSeller.as_view(), name='search_product_seller'),
    path('product/<slug:slug>/<int:id>/', ProductDetail.as_view(), name='detail_product'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='detail_product_not_seller'),

    #Basket Urls
    #path('increase_from_basket/<int:id>/', increase_from_basket, name='increase_from_basket'),
]

