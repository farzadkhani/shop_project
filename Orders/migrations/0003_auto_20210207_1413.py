# Generated by Django 3.1.5 on 2021-02-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20210125_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitems',
            name='user',
        ),
        migrations.AddField(
            model_name='basketitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
