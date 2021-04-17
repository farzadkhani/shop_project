# Generated by Django 3.1.5 on 2021-02-08 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0019_auto_20210208_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Products.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Products.size', verbose_name='Size'),
        ),
    ]