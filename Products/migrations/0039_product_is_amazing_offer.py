# Generated by Django 3.1.5 on 2021-05-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0038_commentdislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_amazing_offer',
            field=models.BooleanField(default=False, verbose_name='پیشنهاد شگفت انگیز'),
        ),
    ]