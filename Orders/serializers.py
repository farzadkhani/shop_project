import os.path
import random
import re
from rest_framework import serializers
from . import models
from Accounts.models import User
from Accounts.serializers import UserModelSerializer



class BasketModelSerializer(serializers.ModelSerializer):
    #just for show.cuse of get the user and product in this json post is dificalt so we write another serializer for that

    # user = UserModelSerializer(read_only=True)
    # # for show user info in comment json we can do this
    # product = ProductSerializer(read_only=True)

    # user_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), write_only=True)
    # # !!! attention: in postman we should use user_id instead write user in json
    # product_id = serializers.PrimaryKeyRelatedField(
    #     queryset=models.Product.objects.all(), write_only=True)
    # # !!! attention: in postman we should use product_id instead write product in json
    # user_detail = UserModelSerializer(source='user', read_only=True)

    # source means show this item in user field ad value
    # sorce by defaul search for the name of the line, hear we rewrited that
    # Product_detail = ProductModelSerializer(source='product', read_only=True)
    class Meta:
        model = models.Basket
        fields = '__all__'

    # def create(self, validated_data):
    #     user_id = validated_data.pop('user_id')
    #     product_id = validated_data.pop('product_id')
    #     return models.Comment.objects.create(**validated_data, user=user_id, product=product_id)

    # def get_image_url(self, obj):
    #     return obj.image.url


class BasketItemsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasketItems
        fields = '__all__'


class OrdersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = '__all__'


class PeymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Peyment
        fields = '__all__'