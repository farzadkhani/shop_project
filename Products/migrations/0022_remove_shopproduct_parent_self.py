# Generated by Django 3.1.5 on 2021-02-17 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0021_auto_20210209_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopproduct',
            name='parent_self',
        ),
    ]
