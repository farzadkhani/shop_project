from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (
    UserModelSerializer, AddressModelSerializer,
    ShopModelSerializer, EmailModelSerializer
)
from .models import (
    User, Address, Shop, Email
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
from .permissions import UserViewPermissions, SuperUserPermissions, ShopPermissions


default_athentication_class = [SessionAuthentication, BasicAuthentication]
# i defind it hear to easy change for deploy


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


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    authentication_classes = default_athentication_class# seas what system we use for authentication
    permission_classes = [UserViewPermissions]# seas what permisions need to access to model
    # permission_classes = [IsAuthenticated or MYCUSTOMPERMISSION]# we can use 2 permision
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        queryset = super(UserModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
        # limit access for users except super users
            return queryset
        elif self.request.user.is_authenticated:
            return queryset.filter(email=self.request.user.email)
        else:
            return queryset.none()

    # def _allowed_methods(self):
    #     if self.request.user.is_authenticated and not self.request.user.is_superuser:
    #         return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    # def limit_create_new_user(self):
    #     if (self.request.user.is_authenticated )and (not self.request.user.is_superuser):
    #         http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    #         return http_method_names
    #     else:
    #         http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    #         return http_method_names

    # @action(detail=True, methods=['GET'])
    # # detail=True means this action just work on detail if detail=False means just work on list
    # def comments(self, request, pk=None):
    #     # pk give if detail=True
    #     product = self.get_object()
    #     # get the object of product
    #     comments = product.Comment.all()
    #     # comments = Comment.objects.filter(product_id=pk)
    #     # comments = Comment.objects.filter(product=product)
    #     serializer = CommentModelSerializer(comments, many=True)
    #     return Response(serializer.data)


class AddressModelViewSet(ModelViewSet):
    serializer_class = AddressModelSerializer
    queryset = Address.objects.all()
    authentication_classes = default_athentication_class
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super(AddressModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return  queryset
        return queryset.filter(user=self.request.user)

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


class ShopModelViewSet(ModelViewSet):
    serializer_class = ShopModelSerializer
    queryset = Shop.objects.all()
    authentication_classes = default_athentication_class
    permission_classes = [ShopPermissions]
    def get_queryset(self):
        queryset = super(ShopModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(is_active=True)
            # return queryset.none()
            # return Shop.objects.none()

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


class EmailModelViewSet(ModelViewSet):
    serializer_class = EmailModelSerializer
    queryset = Email.objects.all()
    authentication_classes = default_athentication_class
    permission_classes = [SuperUserPermissions]


