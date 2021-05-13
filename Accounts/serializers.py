import os.path
import random
import re
from rest_framework import serializers
from . import models


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'


class EmailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'