# Generated by Django 3.1.5 on 2021-02-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_auto_20210207_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]