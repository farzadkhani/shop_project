import os.path
import random
import re
from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class UserModelSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    # invisible password

    @staticmethod
    def validate_password(password: str) -> str:
        # hash password
        return make_password(password)

    class Meta:
        model = models.User
        fields = '__all__'
        # exclude = ('password',)
        # read_only_fields = ('is_activ', ....)
        extra_kwargs = {
            'is_active':{"read_only":True},
            'last_login': {"read_only": True},
            'is_superuser': {"read_only": True},
            'is_staff': {"read_only": True},
            'groups': {"read_only": True},
            'user_permissions': {"read_only": True},
            'date_joined': {"read_only": True},
            'password':{"write_only":True, 'min_length':6, 'required': True, 'allow_blank':False},

            # "username": {"error_messages": {"required": "Give yourself a username"}}
            # "url_field": {"validators": [validators.URLValidator(message="My error message")]}
            # 'email': {'required': True, 'read_only':True},
            # 'email': {'required': True, 'write_only':True},
            # 'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
            # 'users': {'lookup_field': 'username'}
        }
        # action_fields = {
        #     'list': {'fields': ('nickname', 'slug')}
        # }

        # def create(self, validated_data):
        #     password = validated_data.pop('password')
        #     user = super().create(validated_data)
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'
        extra_kwargs = {
            # 'user':{"read_only":True},
        }


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'
        extra_kwargs = {
            'is_active':{"read_only":True},
        }


class EmailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'



