from django.urls import path
from .views import SignUp, LogIn, LogOut, Profile, PersonalDetailEdit, PersonalAddressEdit, remove_address, CreateNewAddress, CreateShop, UpdateShop

from .api import (
    UserModelViewSet, ShopModelViewSet,
    AddressModelViewSet, EmailModelViewSet
)
# from rest_framework.urlpatterns import format_suffix_patterns
from myshopcite.urls import router


router.register(r'accounts/users', UserModelViewSet)
router.register(r'accounts/addresses', AddressModelViewSet)
router.register(r'accounts/shops', ShopModelViewSet)
router.register(r'accounts/emails', EmailModelViewSet)



urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),#jast show the profile of person login
    path('profile/per_edit/', PersonalDetailEdit.as_view(), name='personal_detail_edit'),
    path('profile/address_edit/<str:name>/', PersonalAddressEdit.as_view(), name='personal_address_detail'),
    path('remove_address/<int:id>/', remove_address, name='remove_address'),
    path('create_new_address/', CreateNewAddress.as_view(), name='create_new_address'),
    path('profile/create_shop/', CreateShop.as_view(), name='create_shop'),
    path('profile/update_shop/', UpdateShop.as_view(), name='update_shop'),

]
