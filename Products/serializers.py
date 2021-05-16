import os.path
import random
import re
from rest_framework import serializers
from . import models
from Accounts.models import User
from Accounts.serializers import UserModelSerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.PrimaryKeyRelatedField(
        queryset=models.Brand.objects.all(),
        # error_messages={'does_not_exist': 'Invalid category id'}
        # required=False,
    )
    slug = serializers.SlugField()
    name = serializers.CharField(max_length=500)
    detail = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(
        queryset= models.Category.objects.all(),
        # error_messages={'does_not_exist': 'Invalid category id'}
        # required=False,
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    publish_time = serializers.DateTimeField()
    is_amazing_offer = serializers.BooleanField()

    # validation by exeption handeling
    def validate_slug(self, slug):
        # test slug is unique or not
        try:
            q = models.Product.objects.get(slug=slug)
            raise serializers.ValidationError('ERROR:slug must be uniqe')
        except models.Product.DoesNotExist:
            return slug

    # def validate_mobile(self, mobile):
    #     test = '(^09|^[/+]989|^00989|^009809|^[/+]9809)\d{9}$'
    #     match = re.search((test, mobile))
    #     if not match:
    #         raise serializers.ValidationError(
    #             {"mobile":'invalid mobile number'}
    #         )
    #     test = "(^[/+]989|^989)"
    #     normal_mobile = re.sub(test, "09", mobile)
        # # normalize the mobile number
    #     user = User.objects.filter(mobile=normal_mobile)
    #     if len(user):
    #         raise  serializers.ValidationError(
    #             {"mobile": 'user with this nobile already exists'}, code=400
    #         )
    #     return normal_mobile

    # def validate(self, attrs):
    #     attrs['password'] = str(random.randint(100000, 999999))
    #     return attrs

    # def validate(self, attrs):
    # # "attrs" is attribute, all fields on above is in it. id, brand , slug, name,.....
    #     if attrs['slug'] != attrs['title']:
    #         raise serializers.ValidationError('slug must be same title')
    #
    #     return attrs


    # def validated_slug(self, slug):
    #     if slug.has_child:
    #         raise serializers.ValidationError('wrong category')
    #     return category


    # def validate(self, validated_data):
    #     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     name = self._get_uniq_name()
    #     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    #     images_data = validated_data['html_content']
    #
    #     try:
    #         options = {'crop-h':'1024', 'crop-w': '1024', 'xvfb':''}
    #         img = imgkit.form_string(images_data, file_path, options=options)
    #     except:
    #         options = {'crop-h': '1024', 'crop-w': '1024'}
    #         img = imgkit.form_string(images_data, file_path, options=options)
    #
    #     if imag:
    #         validated_data['img'] = 'media/templates_img/{name}.jpg'.format(name=name)
    #     return validated_data


    # def validate(self, attrs):
    # # "attrs" is attribute, all fields on above is in it. id, brand , slug, name,.....
    #     # return super().validate(attrs)
    #     list_1_id = attrs.get('list_1')
    #     list_1 = []
    #     for item in list_1_id:
    #         try:
    #             list_1.append(List_1.objects.get(id=item))
    #         except List_1 DosNotExist:
    #             raise  NotFound(detail='Error 404, list_1 not found', code=404)
    #     attrs['list_1'] = list_1
    #     attrs['owner'] = list_1[0].owner
    #     return attrs


    def create(self, validated_data):
        '''
        like form we should save that in view now we can save serializer in them class
        "**validated_data" is like Post.objects.create(brand=brand, slug=validated_data['slug'], ...)
        '''
        creator = Product.objects.create(**validated_data)

        return creator

    def update(self, instance, validated_data):
        '''
        like form we should update that in view now we can save serializer in them class
        '''
        instance.slug = validated_data.get('slug', instance.slug)
        instance.name = validated_data.get('name', instance.name)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.publish_time = validated_data.get('publish_time', instance.publish_time)
        instance.save()

        return instance


class ProductModelSerializer(serializers.ModelSerializer):
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
    # # source means show this item in user field ad value
    # # sorce by defaul search for the name of the line, hear we rewrited that

    # comment = serializers.PrimaryKeyRelatedField(
    #     queryset=models.Comment.objects.all()
    # )
    # comment = CommentModelSerializer(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = '__all__'

    # def create(self, validated_data):
    #     user_id = validated_data.pop('user_id')
    #     product_id = validated_data.pop('product_id')
    #     return models.Comment.objects.create(**validated_data, user=user_id, product=product_id)

    # def get_image_url(self, obj):
    #     return obj.image.url


class ProductMetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMeta
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    # parent_detail = CategoryModelSerializer(source='parent', read_only=True)
    class Meta:
        model = models.Category
        # fields = ['name', 'slug', 'detail', 'image', 'parent', 'created_at', 'update_at', 'publish_time']
        fields = '__all__'
        # exclude = ['name', 'slug']


class ShopProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopProduct
        fields = '__all__'


class OffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Off
        fields = '__all__'


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        # fields = '__all__'
        exclude = ['is_active',]


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):

    user_detail = UserModelSerializer(source='user', read_only=True)

    Product_detail = ProductModelSerializer(source='product', read_only=True)

    class Meta:
        model = models.Comment
        # fields = '__all__'
        exclude = ['is_active',]


class CommentLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentLike
        fields = '__all__'


class CommentDisLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentDisLike
        fields = '__all__'


class WishListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'



