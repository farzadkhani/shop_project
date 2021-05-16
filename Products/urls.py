from django.urls import path , include
from .views import (
    ProductListCategory, ProductListSeller, 
    ProductDetail, SearchInProducts, 
    SellerShopProduct, remove_prodcut_from_store, 
    SellerEditShopProduct,
    add_to_wish_list,
    add_to_wish_list_without_id,
    WishListView,
    CommentLikeView,
    CommentDisLikeView,
    EditCommentView,
    remove_from_wish_list,
    )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required

from .api import (
    product_list, product_detail,
    category_detail, category_list,
    CommentList, CommentDetail,
    BrandListMixin, BrandDetailMixin,
    ImagesListGeneric, ImagesDetailGeneric,
    ProductModelViewSet, ProductMetaModelViewSet,
    CategoryModelViewSet, ShopProductModelViewSet,
    OffModelViewSet, BrandModelViewSet,
    ImageModelViewSet, ColorModelViewSet, SizeModelViewSet,
    CommentModelViewSet, WishListModelViewSet,
    CommentLikeModelViewSet, CommentDisLikeModelViewSet
)
# from rest_framework.urlpatterns import format_suffix_patterns
from myshopcite.urls import router


router.register(r'products/products', ProductModelViewSet)
router.register(r'products/product_metas', ProductMetaModelViewSet)
router.register(r'products/categoryes', CategoryModelViewSet)
router.register(r'products/shop_products', ShopProductModelViewSet)
router.register(r'products/offs', OffModelViewSet)
router.register(r'products/brands', BrandModelViewSet)
router.register(r'products/images', ImageModelViewSet)
router.register(r'products/colors', ColorModelViewSet)
router.register(r'products/size', SizeModelViewSet)
router.register(r'products/comments', CommentModelViewSet)
router.register(r'products/comment_likes', CommentLikeModelViewSet)
router.register(r'products/comment_dis_likes', CommentDisLikeModelViewSet)
router.register(r'products/wishlist', WishListModelViewSet)

# we can defind ModelViewSet view urls by router simply
# router import from base urls.py
# attention: we should includ that in Base urlpatterns like[ path('api/', include(router.urls)),]


urlpatterns = [
    path('category/<slug:slug>/', ProductListCategory.as_view(), name='search_product'),
    path('search/', SearchInProducts.as_view(), name='search'),
    path('seller/<slug:slug>/', ProductListSeller.as_view(), name='search_product_seller'),
    path('create_new_product/<str:product>/', SellerShopProduct.as_view(), name='create_new_product'),
    path('edit_product/<slug:slug>/<int:id>/<int:pk>/<str:size>/<str:color>/', SellerEditShopProduct.as_view(), name='edit_product'),
    path('remove_product_from_store/<slug:slug>/<int:pk>/', remove_prodcut_from_store, name='remove_prodcut_from_store'),
    path('product/<slug:slug>/<int:id>/', ProductDetail.as_view(), name='detail_product'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='detail_product_not_seller'),
    path('add_to_wish_list/<slug:slug>/<int:id>/', add_to_wish_list, name='add_to_wish_list'),
    path('add_to_wish_list_without_id/<slug:slug>/', add_to_wish_list_without_id, name='add_to_wish_list_without_id'),
    path('wish_list/', WishListView.as_view(), name='wish_list'),
    path('remove_from_wish_list/<int:id>/', remove_from_wish_list, name='remove_from_wish_list'),
    path('comment_like/<int:pk>/<slug:slug>/<int:id>/', CommentLikeView.as_view(), name='comment_like'),
    path('comment_dislike/<int:pk>/<slug:slug>/<int:id>/', CommentDisLikeView.as_view(), name='comment_dislike'),
    path('edit_comment/<slug:slug>/<int:id>/', EditCommentView.as_view(), name='edit_comment'),
    path('edit_comment/<slug:slug>/', EditCommentView.as_view(), name='edit_comment_not_seller'),




    path('json/products/', product_list, name='json_products_list'),
    path('json/products/<int:pk>/', product_detail, name='json_product_detail'),
    path('json/categories/', category_list, name='json_categories_list'),
    path('json/categories/<int:pk>/', category_detail, name='json_category_detail'),
    path('json/comments/', CommentList.as_view(), name='json_comments_list'),
    path('json/comments/<int:pk>/', CommentDetail.as_view(), name='json_comment_detail'),
    path('json/brands/', BrandListMixin.as_view(), name='json_brands_list'),
    path('json/brands/<int:pk>/', BrandDetailMixin.as_view(), name='json_brand_detail'),
    path('json/images/', ImagesListGeneric.as_view(), name='json_images_list'),
    path('json/images/<int:pk>/', ImagesDetailGeneric.as_view(), name='json_image_detail'),


    # path('json/colors/', ColorModelViewSet.as_view({'get':'list', 'post':'create'}), name='json_colors_list'),
    # path('json/colors/<int:pk>/', ColorModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='json_color_detail'),



    #Basket Urls
    #path('increase_from_basket/<int:id>/', increase_from_basket, name='increase_from_basket'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

