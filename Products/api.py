from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (
    ProductSerializer, ProductModelSerializer,
    CategoryModelSerializer, CommentModelSerializer,
    BrandModelSerializer, ImageModelSerializer,
    ColorModelSerializer, ProductMetaModelSerializer,
    ShopProductModelSerializer, OffModelSerializer,
    SizeModelSerializer, CommentLikeModelSerializer,
    CommentDisLikeModelSerializer, WishListModelSerializer
)
from .models import (
    Product, Brand, Category, Comment, Size, CommentLike,
    Image, Color, ProductMeta, ShopProduct, Off, WishList,
    CommentDisLike
)
from rest_framework.decorators import api_view, action
# decorators: befor execution func decorator get the parameters of func and do some stof on that an pass in function
from rest_framework.response import Response
# this is a rest_framework respons and difrent by respons of djagno
# !!! when we use api_view bether use this response
# safe is not defind for that, automaticly undrestand
# alow us to use api view for browser
from rest_framework import status
# use for http status
from rest_framework.views import APIView
# class based view
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .permissions import (
    JustSuperUserViewPermissions, SuperUserPermissions,
    ShopProductPermissions, ImagePermissions,
    CommentPermissions, WishListPermissions
)




# class CreateUserAPIView(CreateAPIView):
#     """
#     Create a new user.
#     """
#     serializer_class = CreateUserSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#
#         # Create a token that will be used for future auth
#         token = Token.objects.create(user = serializer.instance)
#         token_data = {"token": token.key}
#
#         return Response(
#             {**serializer.data, **token_data},
#             status = status.HTTP_201_CREATED,
#             headers = headers
#         )




@csrf_exempt
def product_list(request):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have POST and GET is one function
    '''
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        # !!!attention: did not add 'data=' befor the "products" , becuse we are not give them data we just wanth get them
        # many=True means this is a several item and not one object, return an array of objects
        return JsonResponse(serializer.data, safe=False)
        # serializer.data meanse change the format of serializer from array to object
        # safe=False should be, it means you sey to django i now it is array and array not safe but you process that
    elif request.method == "POST":
        data = JSONParser().parse(request)
        # hear we get data from request and converting json to dictionary
        serializer = ProductModelSerializer(data=data)
        # !!!attention: did not forget add 'data=' befor the "data"

        if serializer.is_valid():
            serializer.save()
             # hear we call create func we write befor in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have GET, PUT, DELETE is one function
    '''
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return JsonResponse(serializer.data, safe=True)
        # safe should be true becuse in hear we have just one json file and not an array
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductModelSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse(status=204)


@csrf_exempt
@api_view(['GET', 'POST'])
# this decorator get the JSONParser and put it in data parameters automatictly, the proccess like above
# @permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategoryModelSerializer(data=request.data)
        # cuse of api_viiw decorator automaticly create "request.data" and we did not defin that.like this: request['data'] = JSONParser().parse(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    '''
    comment with class based APIView
    '''
    def get(self, request, format=None):
    #
        comments = Comment.objects.all()
        serializer = CommentModelSerializer(comments, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CommentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    '''
    comment with class based APIView
    '''
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandListMixin(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    # this create mixin is create class, list mixin is for list view, generic gave all view necceseries
    serializer_class = BrandModelSerializer
    queryset = Brand.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def perform_create(self, serializer):
    #     # we can do somthing befor save
    #     serializer.save()

class BrandDetailMixin(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    serializer_class = BrandModelSerializer
    queryset = Brand.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ImagesListGeneric(generics.ListCreateAPIView):
    serializer_class = ImageModelSerializer
    queryset = Image.objects.all()


class ImagesDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageModelSerializer
    queryset = Image.objects.all()


class ProductModelViewSet(ModelViewSet):
    # !!! need some edit in URLS
    # have bot list and detail
    # lookup_field = slug
    # # defind which field we want to use, default is pk
    # lookup_url_kwarg = slug
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]

    @action(detail=True, methods=['GET'])
    # detail=True means this action just work on detail if detail=False means just work on list
    def comments(self, request, pk=None):
    # pk give if detail=True
        product = self.get_object()
        # get the object of product
        comments = product.Comment.all()
        # comments = Comment.objects.filter(product_id=pk)
        # comments = Comment.objects.filter(product=product)
        serializer = CommentModelSerializer(comments, many=True)
        return  Response(serializer.data)

    # def perform_create(self, serializer):
    # # autofill the user id for authenticated and superuser
    #     if self.request.user.is_authenticated and not self.request.user.is_superuser:
    #         serializer.save(user=self.request.user)
    #     if self.request.user.is_superuser:
    #         serializer.save()

    # def perform_update(self, serializer):
    # # autofill the user id for authenticated and superuser
    #     if self.request.user.is_authenticated and not self.request.user.is_superuser:
    #         serializer.save(shop=self.request.user.get_shop)
    #     if self.request.user.is_superuser:
    #         serializer.save()

    # def get_queryset(self):
    #     queryset = Color.objects.all()
    #     queryset = queryset.filter(draft=False)
    #     return queryset

    # @action(detail=True, methods=['GET'])
    # # detail=True means this action just work on detail if detail=False means just work on list
    # def comments(self, request, pk=None):
    # # pk give if detail=True
    #     product = self.get_object()
    #     # get the object of product
    #     # comments = product.Comment.all()
    #     # comments = Comment.objects.filter(product_id=pk)
    #     comments = Comment.objects.filter(product=product)
    #     serializer = CommentModelViewSet(comments, many=True)
    #     return  Response(serializer.data)


    # @action(detail=False, methods=['GET'])
    # # extraAction for get product has draft=false
    # def get_published(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     queryset = queryset.filter(draft=False)
    #     page = self.paginate_queryset(queryset)
    #       # we can paginate that
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(detail=True, methods=['POST'])
    # # extraAction for publishe product
    # # did not work in browserAPI, should use PostMan
    # def publish(self, request, pk=None):
    #     product = self.get_object()
    #     product.is_draft = False
    #     product.save()
    #     serializer = sef.get_serializer(product)
    #     return Response(serializer.data)


class ProductMetaModelViewSet(ModelViewSet):
    serializer_class = ProductMetaModelSerializer
    queryset = ProductMeta.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]


class ShopProductModelViewSet(ModelViewSet):
    serializer_class = ShopProductModelSerializer
    queryset = ShopProduct.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [ShopProductPermissions]

    def perform_create(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(shop=self.request.user.get_shop)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(shop=self.request.user.get_shop)
        if self.request.user.is_superuser:
            serializer.save()


class OffModelViewSet(ModelViewSet):
    serializer_class = OffModelSerializer
    queryset = Off.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [JustSuperUserViewPermissions]


class BrandModelViewSet(ModelViewSet):
    serializer_class = BrandModelSerializer
    queryset = Brand.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]


class ImageModelViewSet(ModelViewSet):
    serializer_class = ImageModelSerializer
    queryset = Image.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [ImagePermissions]

    def perform_create(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(shop=self.request.user.get_shop)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(shop=self.request.user.get_shop)
        if self.request.user.is_superuser:
            serializer.save()


class ColorModelViewSet(ModelViewSet):
    serializer_class = ColorModelSerializer
    queryset = Color.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]


class SizeModelViewSet(ModelViewSet):
    serializer_class = SizeModelSerializer
    queryset = Size.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [SuperUserPermissions]


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        queryset = super(CommentModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
        # limit access for users except super users
            return queryset
        else:
            return queryset.filter(is_active=True)

    def perform_create(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
    # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()


class CommentLikeModelViewSet(ModelViewSet):
    serializer_class = CommentLikeModelSerializer
    queryset = CommentLike.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        queryset = super(CommentLikeModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
        # limit access for users except super users
            return queryset
        else:
            return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()


class CommentDisLikeModelViewSet(ModelViewSet):
    serializer_class = CommentDisLikeModelSerializer
    queryset = CommentDisLike.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        queryset = super(CommentDisLikeModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
        # limit access for users except super users
            return queryset
        else:
            return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()


class WishListModelViewSet(ModelViewSet):
    serializer_class = WishListModelSerializer
    queryset = WishList.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [WishListPermissions]

    def get_queryset(self):
        queryset = super(WishListModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
        # limit access for users except super users
            return queryset
        elif self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        else:
            return queryset.none()

    def perform_create(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        if self.request.user.is_superuser:
            serializer.save()


