# Generated by Django 3.1.5 on 2021-05-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0041_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='product detail'),
        ),
    ]
