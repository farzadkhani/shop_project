from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (
    BasketModelSerializer, OrdersModelSerializer,
    BasketItemsModelSerializer, PeymentModelSerializer
)
from .models import (
    Basket, BasketItems, Orders, Peyment
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
    SuperUserPermissions, JustSuperUserViewPermissions,
    BasketPermissions, BasketItemPermissions
)






class BasketModelViewSet(ModelViewSet):
    serializer_class = BasketModelSerializer
    queryset = Basket.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [BasketPermissions]
    #
    def get_queryset(self):
        queryset = super(BasketModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return queryset
        elif self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        else:
            return queryset.none()
    #
    # def perform_create(self, serializer):
    #     # autofill the user id for authenticated and superuser
    #     if self.request.user.is_authenticated and not self.request.user.is_superuser:
    #         serializer.save(user=self.request.user)
    #     if self.request.user.is_superuser:
    #         serializer.save()
    #
    # def perform_update(self, serializer):
    #     # autofill the user id for authenticated and superuser
    #     if self.request.user.is_authenticated and not self.request.user.is_superuser:
    #         serializer.save(user=self.request.user)
    #     if self.request.user.is_superuser:
    #         serializer.save()


class BasketItemModelViewSet(ModelViewSet):
    serializer_class = BasketItemsModelSerializer
    queryset = BasketItems.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [BasketItemPermissions]

    def get_queryset(self):
        queryset = super(BasketItemModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return queryset
        elif self.request.user.is_authenticated:
            return queryset.filter(basket__user=self.request.user)
        else:
            return queryset.none()

    def perform_create(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(basket=self.request.user.get_basket)
        if self.request.user.is_superuser:
            serializer.save()

    def perform_update(self, serializer):
        # autofill the user id for authenticated and superuser
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            serializer.save(basket=self.request.user.get_basket)
        if self.request.user.is_superuser:
            serializer.save()


class OrdersModelViewSet(ModelViewSet):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [JustSuperUserViewPermissions]


class PeymentModelViewSet(ModelViewSet):
    serializer_class = PeymentModelSerializer
    queryset = Peyment.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [JustSuperUserViewPermissions]


