# Generated by Django 3.1.5 on 2021-02-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20210206_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=1000, unique=True, verbose_name='name'),
        ),
    ]
