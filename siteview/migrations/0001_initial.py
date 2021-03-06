# Generated by Django 3.1.5 on 2021-01-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    # dependencies = [
    #     ('siteview', '0004_auto_20210124_0642'),
    # ]
    #
    # operations = [
    #     migrations.AddField(
    #         model_name='firstslideindex',
    #         name='draft',
    #         field=models.BooleanField(db_index=True, default=True, verbose_name='Draft'),
    #     ),
    # ]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstSlideIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='siteview/firstslideindex/images', verbose_name='image')),
                ('title_one', models.CharField(max_length=500, verbose_name='product title one')),
                ('title_two', models.CharField(max_length=500, verbose_name='product title two')),
                ('detail', models.CharField(max_length=500, verbose_name='product detail')),
                ('draft', models.BooleanField(db_index=True, default=True, verbose_name='Draft')),
            ],
            options={
                'verbose_name': 'FirstSlideIndex',
                'verbose_name_plural': 'FirstSlideIndex',
            },
        ),
    ]