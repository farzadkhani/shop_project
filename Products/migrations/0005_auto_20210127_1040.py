# Generated by Django 3.1.5 on 2021-01-27 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20210127_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', related_query_name='children', to='Products.category', verbose_name='Parent'),
        ),
    ]
