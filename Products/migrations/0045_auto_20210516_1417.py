# Generated by Django 3.1.5 on 2021-05-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_auto_20210516_1155'),
        ('Products', '0044_auto_20210516_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmeta',
            options={'ordering': ['-id'], 'verbose_name': 'ProductMeta', 'verbose_name_plural': 'ProductMetas'},
        ),
        migrations.AlterModelOptions(
            name='shopproduct',
            options={'ordering': ['-id'], 'verbose_name': 'ShopProduct', 'verbose_name_plural': 'ShopProducts'},
        ),
        migrations.AddField(
            model_name='image',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Image', related_query_name='Image', to='Accounts.shop', verbose_name='Shop'),
        ),
    ]
