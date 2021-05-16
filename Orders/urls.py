from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BasketItemList, remove_from_basket, decrease_from_basket, increase_from_basket, add_to_basket



from .api import (
    BasketModelViewSet, BasketItemModelViewSet,
    OrdersModelViewSet, PeymentModelViewSet
)
from myshopcite.urls import router


router.register(r'orders/baskets', BasketModelViewSet)
router.register(r'orders/basket_items', BasketItemModelViewSet)
router.register(r'orders/orders', OrdersModelViewSet)
router.register(r'orders/peyments', PeymentModelViewSet)



urlpatterns = [
    #Basket Urls
    path('basket/', BasketItemList.as_view(), name='basket'),
    path('add_to_basket/<int:id>/<slug:slug>/', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:id>/', remove_from_basket, name='remove_from_basket'),
    path('decrease_from_basket/<int:id>/', decrease_from_basket, name='decrease_from_basket'),
    path('increase_from_basket/<int:id>/', increase_from_basket, name='increase_from_basket'),


    #BasketItem Urls

    
]