# Generated by Django 3.1.5 on 2021-01-21 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='', verbose_name='Brand name')),
                ('details', models.CharField(max_length=2000, verbose_name='Brand details')),
                ('image', models.ImageField(upload_to='Products/brand/images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='product name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('details', models.CharField(max_length=2000, verbose_name='cateqory detail')),
                ('image', models.ImageField(upload_to='Products/category/images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='Products.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('name', models.CharField(max_length=500, verbose_name='product name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='orders/product/images', verbose_name='image')),
                ('detail', models.CharField(max_length=2000, verbose_name='product detail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', related_query_name='brand', to='Products.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='Products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='product price')),
                ('quantity', models.IntegerField(verbose_name='number of product')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='Products.product', verbose_name='Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Accounts.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'shop stor',
                'verbose_name_plural': 'shop stor',
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_meta', related_query_name='product_meta', to='Products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'ProductMeta',
                'verbose_name_plural': 'ProductMeta',
            },
        ),
        migrations.CreateModel(
            name='Off',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='off name')),
                ('number', models.IntegerField(verbose_name='number of price off')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Off', related_query_name='Off', to='Products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'off',
                'verbose_name_plural': 'offes',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, verbose_name='like')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='likes', to='Products.product', verbose_name='Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', related_query_name='like', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Like',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Products/images/images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='images', to='Products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to='Products.product', verbose_name='Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]