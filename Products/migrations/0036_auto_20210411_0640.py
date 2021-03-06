# Generated by Django 3.1.5 on 2021-04-11 06:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0035_auto_20210411_0559'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
    ]
