# Generated by Django 3.1.5 on 2021-04-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_auto_20210403_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
    ]
